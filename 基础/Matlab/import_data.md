## Matlab
### Create Table
```
LastName = {'Smith';'Johnson';'Williams';'Jones';'Brown'};
Age = [38;43;38;40;49];
Height = [71;69;64;67;64];
Weight = [176;163;131;133;119];
BloodPressure = [124 93; 109 77; 125 83; 117 75; 122 80];

T = table(Age,Height,Weight,BloodPressure,'RowNames',LastName)
```
T = 

                Age    Height    Weight    BloodPressure
                ___    ______    ______    _____________

    Smith       38     71        176       124     93   
    Johnson     43     69        163       109     77   
    Williams    38     64        131       125     83   
    Jones       40     67        133       117     75   
    Brown       49     64        119       122     80 

```
Date = {'12/25/11','1/2/12','1/23/12','2/7/12','2/15/12'};
location1 = [20 5 13 0 17];
location2 = [18 9 21 5 12];
location3 = [26 10 16 3 15];

T = table;
T.Date = Date';
T.Natick = location1';
T.Boston = location2';
T.Worcester = location3'
```
T = 

       Date       Natick    Boston    Worcester
    __________    ______    ______    _________

    '12/25/11'    20        18        26       
    '1/2/12'       5         9        10       
    '1/23/12'     13        21        16       
    '2/7/12'       0         5         3       
    '2/15/12'     17        12        15 

## Read Table
opts = detectImportOptions()
readtable('', opts)


```
readtable()
```

### BigData
1. matlab

| datastore | tall | gather |

2. mapreduce
| datastore | mapfun | reducefun |

```
# mapfun
function myMapper(data, info, intermKVStore)
%do a calculation with the data chunk
add(intermKVStore, key, value)
end

# reducefun
function myReducer(intermKey, intermValIter, outKVStore)
while hasnext(intermValIter)
    X = getnext(intermValIter);
    %do a calculation with the current value, X
end
add(outKVStore, key, value)
end
```
