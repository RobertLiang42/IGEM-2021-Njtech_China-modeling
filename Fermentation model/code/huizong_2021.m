clc
clear
%% 数据读取
data=xlsread('C:\Users\王济坤\Desktop\IGEM建模\发酵（数模）(1).xlsx')';
t=0:12:120;
t=t';
C=data(:,1);%这里改变1,2可以计算1,2组
S=data(:,5);%这里改变1,2可以计算1,2组
P=data(:,9);%这里改变1,2可以计算1,2组

%% 画图
figure(1)
[ax,h1,h2]=plotyy(t,P,[t,t],[C,S]);
set(h1,'marker','o','linewidth',1.5)
set(h2(1),'marker','s','linewidth',1.5)
set(h2(2),'marker','^','linewidth',1.5)
set(get(ax(1),'Ylabel'),'string','2-PE（g/L）')
set(get(ax(2),'Ylabel'),'string','OD_6_0_0 , L-Phe（g/L）')
set(gcf,'color',[1 1 1]);
xlabel('Time（h）')
legend('2-PE','OD_6_0_0','L-Phe')
title('Shake flask fermentation curve')
grid on
