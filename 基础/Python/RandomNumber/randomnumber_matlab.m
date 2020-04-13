%% random number
% uniformly distributed random numbers between 0 and 1
rand()
% Generate a 5-by-5 matrix of uniformly distributed random numbers between 0 and 1
rand(5)
rand(3, 5)
% Generate a 10-by-1 column vector of uniformly distributed numbers in the interval (-5,5)
% r = a + (b-a).*rand(N,1)
10 * rand(10, 1) - 5
% random integer
% Use the randi function (instead of rand) to generate 5 random integers from the uniform distribution between 10 and 50
randi([10,50],1,5)

% random Gaussian distribution
% Generate a 5-by-5 matrix of normally distributed random numbers
randn(5,4)
% random permutation
randperm(10)
randperm(10,4)


