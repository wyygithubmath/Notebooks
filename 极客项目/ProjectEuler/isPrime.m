% number is a prime
function y = isPrime(x)
    flag = 0;
    if x <= 1
        flag = 0;
    else
        for k = 1:floor(sqrt(x))
            if mod(x, k) == 0
                flag = 0;
            else
                flag = 1;
            end
        end
    end
     y = flag;
end