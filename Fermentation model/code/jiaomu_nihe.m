function [fitresult, gof] = jiaomu_nihe(t1, y1)
%CREATEFIT(T1,Y1)
%  Create a fit.
%
%  Data for 'untitled fit 1' fit:
%      X Input : t1
%      Y Output: y1
%  Output:
%      fitresult : a fit object representing the fit.
%      gof : structure with goodness-of fit info.
%
%  另请参阅 FIT, CFIT, SFIT.

%  由 MATLAB 于 18-Aug-2021 20:59:48 自动生成


%% Fit: 'untitled fit 1'.
[xData, yData] = prepareCurveData( t1, y1 );

% Set up fittype and options.
ft = fittype( 'poly1' );

% Fit model to data.
[fitresult, gof] = fit( xData, yData, ft );

% Plot fit with data.
figure( 'Name', 'untitled fit 1' );
h = plot( fitresult, xData, yData );
set(h,'linewidth',1.5)

% legend( h, 'y1 vs. t1', 'untitled fit 1', 'Location', 'NorthEast', 'Interpreter', 'none' );
% Label axes
xlabel( '时间', 'Interpreter', 'none' );
ylabel( 'ln[C/(Cmax-C)]', 'Interpreter', 'none' );
title('ln[C/(Cmax-C)]与t的关系')
grid on


