clear
clc

%% 数据准备
% 导入数据
% readtable detectImportOption
% ops = detectImportOptions('./boston.csv');
% T = readtable('./boston.csv');
% summary(T)
dt = csvread('./boston.csv', 1, 0);
[r, c] = size(dt);

boston_data = dt(1:end, 1:c-1);
boston_target = dt(1:end, c);

% 分割数据
percent = floor(r * 0.7);
train_data = boston_data(1:percent, 1:end);
train_target = boston_target(1:percent);
test_data = boston_data(percent+1:end, 1:end);
test_target = boston_target(percent+1:end);

% 线性回归
model = fitlm(train_data, train_target);

%% 自己实现
flag = det(train_data'*train_data);
temp = [ones(percent, 1) train_data];
w = temp'*temp \ (temp'*train_target);
se = (train_target - temp*w)'*(train_target - temp*w);














