clear

%% import data
data =  dlmread('./machinelearninginaction/1/datingTestSet2.csv', ',');
size(data)

%% Plot 
scatter(data(1:1000,1),data(1:1000,2),[],data(1:1000,4))

%% kNN
% Cross validate the KNN classifier using the default 10-fold cross validation
kNN_mat = fitcknn(data(1:800, 1:3),data(1:800,4),'Distance','euclidean','NumNeighbors',5,'Standardize',1)
y_pre = kNN_mat.predict(data(801:1000, 1:3));
wrongnumber = sum(y_pre ~= data(801:1000,4))
rightrate = 1 - sum(y_pre ~= data(801:1000,4)) / 200
% Cross validate the KNN classifier using the default 10-fold cross validation
kNN_mat_c = crossval(kNN_mat,'kfold',10);
classError = kfoldLoss(kNN_mat_c)

%% own distance function


%% own coding


