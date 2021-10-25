clc;
clear;
%%区域离散化（注意：dxdx不能取太小，考虑模型稳定性）
dx=0.05;
Lx=5;
x=0:dx:Lx;
dy=0.05;
Ly=5;
y=0:dy:Ly;
dt=0.0001;
t=-5:dt:10;
C_0=0.4304;
C_max=25.79;
miu=1.2350;

C_x=(C_0*C_max*exp(miu.*t))./(C_max-C_0+C_0*exp(miu*t)).*(exp(-t)*4-1);

%%矩阵运算
A1=-2*eye(length(x))+diag(ones(1,length(x)-1),1)+diag(ones(1,length(x)-1),-1);
% A1(1,end)=1;A1(end,1)=1;%周期性边界条件
A2=-2*eye(length(y))+diag(ones(1,length(y)-1),1)+diag(ones(1,length(y)-1),-1);
% A2(1,end)=1;A2(end,1)=1;%周期性边界条件
%%准备阶段
[X,Y]=meshgrid(x,y);
U=zeros(length(y),length(x));%思考为什么y在前x在后
%%两个热源
f1=zeros(length(y),length(x));

f1(round(length(x)/2)-2:round(length(x)/2)+2,round(length(y)/2)-2:round(length(y)/2)+2)=C_x(1);

%%
U0=0*exp(-10*((X-Lx/2).^2+(Y-Ly/2).^2));%初值条件
U(:,:)=U0;
a=1;
% aviobj=VideoWriter('jiaomu.avi');%新建叫example.avi的文件
% open(aviobj); %打开
for n=1:length(t)-1
    
    U(:,:)=U(:,:)+a^2*(1/dx^2*U(:,:)*A1+1/dy^2*A2*U(:,:)+...
        15*f1(:,:))*dt;%注意这里加入随时间变化的扩散源
    U(:,1)=U(:,2);%四边绝热
    U(:,end)=U(:,end-1);%如果没有给边界条件就是默认边界为0
    U(end,:)=U(end-1,:);
    U(1,:)=U(2,:);
    f1(round(length(x)/2),round(length(y)/2))=C_x(n+1);
    if mod(n,1000)==1
        figure(1)
        surf(X,Y,U(:,:));
        colormap(jet),colorbar
        caxis([0.001,0.26])
        axis equal
        axis([x(1) x(end) y(1) y(end) -0.5 4])
        view(0,90)
        shading interp
        
        currFrame = getframe;
%         writeVideo(aviobj,currFrame);
    end
    
 end
%  close(aviobj); %关闭




