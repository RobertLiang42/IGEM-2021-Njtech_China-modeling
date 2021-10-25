clc
clear
%% 数据读取
data=xlsread('C:\Users\王济坤\Desktop\IGEM建模\发酵（数模）(1).xlsx')';
t=0:12:120;
t=t';
P=data(:,9);%这里改变1,2可以计算1,2组

%% 参数
C=data(:,1);%这里改变1,2可以计算1,2组
C_max=max(C);%C_max的参数
C_0=C(1);%C_0的参数
mf1=@(miu_max,t)(C_0*C_max*exp(miu_max*t))./(C_max-C_0+C_0*exp(miu_max*t));
miu_max=lsqcurvefit(mf1,rand(1,1),t,C)%miu_max的参数

%% 拟合

mf3=@ (cs,t)cs(1)*C_0*((exp(miu_max.*t))./(1-C_0/C_max*(1-exp(miu_max*t)))-1)+cs(2)*C_max/miu_max*log(1-C_0/C_max*(1-exp(miu_max.*t)));
cs=lsqcurvefit(mf3,rand(2,1),t,P);
figure(1)
plot(t,cs(1)*C_0*((exp(miu_max.*t))./(1-C_0/C_max*(1-exp(miu_max*t)))-1)+cs(2)*C_max/miu_max*log(1-C_0/C_max*(1-exp(miu_max.*t))),'r-s','linewidth',1.5,'markerfacecolor','b')
hold on
plot(t,P,'d','markersize',6,'markerfacecolor','c')
xlabel('Time (h)')
ylabel('2-PE (g/L)')
legend('Model value','Experimental value')
title('Comparison of model value and experimental value of 2-PE production')
set(gcf,'color',[1 1 1]);
grid on

%% 画图
A_t=C_0*((exp(miu_max.*t))./(1-C_0/C_max*(1-exp(miu_max*t)))-1);
B_t=C_max/miu_max*log(1-C_0/C_max*(1-exp(miu_max.*t)));
x=A_t;
y=P-cs(2)*B_t;
figure(2)
plot(x,y,'o','markerfacecolor','r')
hold on
plot(x,cs(1)*x,'b-','linewidth',1.5)
xlabel( 'A(t)', 'Interpreter', 'none' );
ylabel( 'P-βB(t)', 'Interpreter', 'none' );
title('P-βB(t)—A(t)')
grid on

%%参数输出
C_max
C_0
miu_max
cs