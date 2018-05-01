#输出全排列
def QPL(m_list):
    if len(m_list) == 1:
        yield m_list
    for i in range(len(m_list)):
        restlist = m_list[0:i]+m_list[i+1:]
        for subres in QPL(restlist):
            yield [m_list[i]]+subres;
 
#判断质数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
     
for t in QPL(range(7,0,-1)):
    if t[-1] != 1 and t[-1] != 3 and t[-1] != 7:
        continue;
    k = int(''.join(map(str,t)));
    if isPrime(k):
        print k
        break
