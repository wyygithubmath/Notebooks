# Project Euler

1. 函数式
   + MMA
   + Haskell
2. 命令式
   + Python
   + Matlab

### Prolem 1

1. Python

``` python
a = [i for i range(3, 100) if i / 3 == 0 and i / 5 == 0]
sum(a)
```

2. Matlab

``` matlab
a = 1:100;
sum(a())
```

3. Mathematica

``` Mathematica
a = Table[i, {i, 1, 999}]
Select[a,Mod[#,3]==0 || Mod[#,5]==0&]//Total
```

4. Haskell

``` Haskell
a = [i | i <- [1 .. 100], i / 5 == 0 && i / 3 == 0]
sum a
```

### Prolem 2

> Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
> 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
> By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

1. Python

```python

```

2. Mathematica

```mathematica
Select[Table[Fibonacci[n], {n, 1, 50}], EvenQ[#] && # <= 1000000 &] // Total
```






