# Haskell

1. Haskell Platform 8.2.1
   + 解释器 GCHi
   + 标准库
   + 第三方库 HackageDB
   + 打包发布工具 Cabal


```haskell
:set prompt "ghci>"
```




## 基本类型
### 1. 类型
| Bool        | 整数      | 字符               | 浮点                  |
| ----------- | ------- | ---------------- | ------------------- |
| True        | Integer | Char  'a'        | Float/Double        |
| False       | Int     | String "a" "abc" | Rational            |
| && \|\| not |         | show/read        | ceiling/floor/round |
|             |         |                  |                     |
|             |         |                  |                     |

```haskell
read "5" :: Int
read "5" :: Float
```

#### Transform

```haskell
fromInteger 5 :: Float
```
Type Class
| Eq   | Ord  | Enum | Bounded | Show | Num  |
| ---- | ---- | ---- | ------- | ---- | ---- |
|      | L    |      |         | Read |      |

```haskell
type RGB = (Int, Int, Int)
type Picture = [[RGB]]
```


### 2. List
#### 生成列表

```haskell
-- ghci
let lostNumbers = [4, 8, 15, 16, 23, 48]
-- script
lostNumbers = [4, 8, 15, 16, 23, 48]
-- Operation
[1, 2, 3, 4] ++ [9, 10, 11, 12]
1:[2, 3, 4, 5]
"My Little Daught" !! 6
```

1. ++
2. :
3. !!
4. function

| head   | init    | last   | tail | take | drop |
| ------ | ------- | ------ | ---- | ---- | ---- |
| length | null    | `elem` |      |      |      |
| sum    | product |        |      |      |      |

#### 无限列表
```haskell
[1 .. 20]
['A' .. 'Z']
[1, 3 .. 20]
-- 避免在 Range 中使用浮点数
-- 无限列表
take 13 [13, 26, .. ]
take 5 (cycle [1, 2, 3])
take 10 (repeat 5)
replicate 10 5
```

| cycle | repeat | replicate |
| ----- | ------ | --------- |
|       |        |           |

#### list comprehension

```haskell
[x*2 | x <- [1 .. 10], x*2 > 12]
```

### Tuple

1. fst
2. snd
3. zip


```haskell
(1, 2)
('a', 'b', 'c')
zip () ()
```



## 表达式与值

| 表达式(expression) | 计算(evaluate) | 值(value) |
| --------------- | ------------ | -------- |
| (7 - 3) * 2     |              | 8        |

## 函数程序

1. 函数声明
2. 函数调用

```haskell
div 92 9
92 `div` 9
{- 
name :: type
name = expression 
-}
size :: Integer
size = 12 + 13
-- funxtion
square :: Num a => a -> a
squre n = n * n 
```



| 函数     |        作用        |   标准库   |
| ------ | :--------------: | :-----: |
| t      |      :t sum      | Prelude |
| set    | :set editor vim  |         |
| edit   |  :edit first.hs  |         |
| module | :m  +/-Data.Word |         |
|        |                  |         |
|        |                  |         |

 ###  $\lambda$ expression

