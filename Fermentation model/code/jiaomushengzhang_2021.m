clc
clear
%% 数据读取
data=xlsread('C:\Users\王济坤\Desktop\IGEM建模\发酵（数模）(1).xlsx')';
t=0:12:120;
C=data(:,1);%这里改变1,2可以计算1,2组
C_max=max(C);
C_0=C(1);


%% 拟合
figure(1)
mf1=@(miu_max,t)(C_0*C_max*exp(miu_max*t))./(C_max-C_0+C_0*exp(miu_max*t));
miu_max=lsqcurvefit(mf1,rand(1,1),t',C);
plot(t,C,'^','markersize',6,'markerfacecolor','g')
hold on
plot(t,(C_0*C_max*exp(miu_max*t))./(C_max-C_0+C_0*exp(miu_max*t)),'-o','linewidth',1.5)
xlabel('Time（h）')
ylabel('OD_6_0_0')
legend('Model value','Experimental value')
grid on
set(gcf,'color',[1 1 1]);
title('Comparison of model value and experimental value of Yeast growth')
%% 画图

C_max=max(C);
y=log(C(1:5)./(C_max-C(1:5)));
x=t(1:5);
b=-log(C_max/C_0-1);
figure(2)
plot(x,miu_max*x+b,'-','linewidth',1.5)
hold on
plot(x(1:5),y(1:5),'o','markerfacecolor','r')
xlabel( 't', 'Interpreter', 'none' );
ylabel( 'ln[C/(Cmax-C)]', 'Interpreter', 'none' );
title('ln[C/(Cmax-C)]-t')
grid on
%% 参数输出
C_max
C_0
miu_max
b
