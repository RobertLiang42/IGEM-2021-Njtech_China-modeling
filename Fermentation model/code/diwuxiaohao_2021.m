clc
clear
%% 数据读取
data=xlsread('C:\Users\王济坤\Desktop\IGEM建模\发酵（数模）(1).xlsx')';
t=0:12:120;
t=t';
S=data(:,5);%这里改变1,2可以计算1,2组
%% 参数
C=data(:,1);%这里改变1,2可以计算1,2组
C_max=max(C);%C_max的参数
C_0=C(1);%C_0的参数
mf1=@(miu_max,t)(C_0*C_max*exp(miu_max*t))./(C_max-C_0+C_0*exp(miu_max*t));
miu_max=lsqcurvefit(mf1,rand(1,1),t,C)%miu_max的参数
%% 拟合
S_0=S(1);
mf2=@(a,t)S_0-a(1)*C_0*((exp(miu_max.*t))./(1-C_0/C_max*(1-exp(miu_max*t)))-1)+a(2)*C_max/miu_max*log(1-C_0/C_max*(1-exp(miu_max.*t)));
a=lsqcurvefit(mf2,rand(2,1),t,S);
figure(1)
plot(t,S_0-a(1)*C_0*((exp(miu_max.*t))./(1-C_0/C_max*(1-exp(miu_max*t)))-1)+a(2)*C_max/miu_max*log(1-C_0/C_max*(1-exp(miu_max.*t))),'o-','linewidth',1.5,'markerfacecolor','r')
hold on
plot(t,S,'>','markersize',6,'markerfacecolor','y')
xlabel('Time (h)')
ylabel('L-Phe（g/L）')
legend('Model value','Experimental value')
title('Comparison of model value and experimental value of L-Phe consumption')
set(gcf,'color',[1 1 1]);
grid on

%% 画图
figure(2)
M_t=C_0*((exp(miu_max.*t))./(1-C_0/C_max*(1-exp(miu_max*t)))-1);
N_t=C_max/miu_max*log(1-C_0/C_max*(1-exp(miu_max.*t)));
y=S_0-S+a(2)*N_t;
x=M_t;
plot(x,y,'o','markerfacecolor','r')
hold on
plot(x,a(1)*x,'b-','linewidth',1.5)
grid on
xlabel( 'M(t)', 'Interpreter', 'none' );
ylabel( 'S_0-S-δN(t)', 'Interpreter', 'none' );
title('S_0-S-δN(t)—M(t)')
grid on

%% 参数输出
C_max
C_0
miu_max
S_0
a