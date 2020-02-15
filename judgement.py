import math
import time
class Polynomial :
    ord = 5
    pol=[]
    
    def __init__(self,a,b=[]):
        self.ord = a
        self.pol = b

    # 构造多项式类
    def pol_s_in(self,a,b=""):
        self.ord = a
        sum = 0
        i = 0
        while (i<len(b) and b[i]!='+'):
            sum = 0
            o = 0
            while (i<len(b) and b[i] <= '9' and b[i]>= '0'):
                sum = sum*10 +int(b[i])
                i = i+1
            if (sum == 0):
                sum = 1
            if (i<len(b) and b[i] == 'x'):
                i = i+1
                if (i<len(b) and b[i]=='^'):
                    i = i+1
                    while (i<len(b) and b[i]<='9' and b[i]>= '0'):
                        o = o*10 +int(b[i])
                        i = i+1
                else:
                    o = 1
            if(len(self.pol)<o+1):
                self.pol = [0]*(o+1)
            self.pol[o] = sum
            i= i+1     


    def is_zero(self):
        if (len(self.pol)==0):
            return True
        return False

    # 判断多项式是否不可约
    def is_irr(self):
       p = Polynomial(5, self.pol)
       vFac = []
       pOrd = len(self.pol)-1 # 多项式的次数
       if pOrd == 1:
           return True
       Q1 = Polynomial(5,[1]) # 多项式 1
        # step 1
       if((fastExponentialAlgorithm(p,len(self.pol)-1)==Q1)==False):     
           return False
        # -----------------------
        # step 2
       for i in range(self.ord):
           n = i
           sum = 0 
           for j in range(1,len(self.pol)):
               if i != 0 :
                   sum = ((sum + self.pol[j]*i**j) % self.ord +self.ord) %self.ord
           sum = ((sum +self.pol[0])% self.ord +self.ord) %self.ord
           if (sum == 0):
               return False
        # -----------------------------
        # step 3
       vFac = factorization(len(self.pol)-1)
       for i in range(len(vFac)):
           ll = [0]*(5**(pOrd// vFac[i])-1)
           ll.append(1)
           pd = Polynomial(5,ll)
           pd.pol[0]=-1
           if(((EuclideanAlgorithm(pd, p) == Q1 ) == False) or ((EuclideanAlgorithm(p, pd) == Q1 ) == False) ):
               return False
        # ------------------------------------
       return True
        


    # 判断是否为本原多项式
    def is_pri(self):
        pass

    # 重载取余运算符
    def __mod__(self,other):
        m = self.pol
        n = other.pol
        coe = 0
        if len(m)<len(n):
            return self
        for i in range(len(m)-len(n)+1):
            coe = 0
            ma = m[len(m)-1-i]
            while(len(n) >0 and coe == 0):
                if ma % n[-1]==0:
                    coe = ma//n[-1]
                ma = ma+self.ord
            for j in range(len(n)):
                m[len(m)-1-i-j]=(m[len(m) - 1 - i - j] - coe * n[len(n) - 1 - j] % self.ord + self.ord) % self.ord
        while (len(m)!=0) and (m[-1]==0):
            m.pop()
        return Polynomial(self.ord, m)

       
    # 重载乘法运算符
    def __mul__(self,other):
        ma = self.pol
        mb = other.pol
        mc = [0]*(len(ma)+len(mb)-1)
        for i in range(len(ma)):
            for j in range(len(mb)):
                mc[i+j]=((mc[i+j]+ma[i]*mb[j]) % self.ord+self.ord) % self.ord
        c = Polynomial(self.ord, mc)
        return c


    # 重载比较运算符   
    def __eq__(self,other):
        if (self.ord == other.ord) and (self.pol == other.pol):
            return True
        return False




# 欧几里得算法
def EuclideanAlgorithm(a,b):
    pa = a 
    pb = b  
    while (pb.is_zero()==False):
        pc = pa % pb
        pa = pb
        pb = pc
    if (len(pa.pol)==1):
        pa.pol = [1]
    return pa

# 快速指数算法
def fastExponentialAlgorithm(a,b):
    sum = a.ord**b
    # vBin = []
    Q1 = Polynomial(5,[1])
    Qx = Polynomial(5,[0,1])
    qm = Q1
    
    sum = sum -1
    # while(sum!=0):
    #     vBin.append(sum % 2)
    #     sum = sum//2
    # for i in range((len(vBin)-1),-1,-1):
        # qm = (qm*qm) % a
        # if(vBin[i]):
        #     qm = (qm * Qx) % a
        # if qm.is_zero:
        #     break
    l = [0]*sum
    l.append(1) 
    pp = Polynomial(5,l)
    qm = pp % a
    
    return qm

# 对 n 唯一分解 
def factorization(n):
    a = []
    for i in range(2,int((n/2)+1)):
        if (n % i == 0) and is_prime_number(i):
            a.append(i)

    if len(a)==0:
        a.append(n)
    return a

# 判断素数
def is_prime_number(n):
    flag = 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            flag = flag+1
        if flag > 0:
            return False
    return True

def trans_map(cint):
    if cint < 0:
        print("不合法")
        return
    elif cint < 10:
        return cint

    elif cint >= 10:
        return chr(cint - 10 + 65)



def tenToAny(n, origin):
    # 10进制转换为任意进制的数
    list = []
    while True:
        # 取商
        s = origin // n
        # 取余数
        tmp = origin % n
        list.append(trans_map(tmp))
        if s == 0:
            break
        origin = s
    list.reverse()
    list = [str(each) for each in list]
    num = ''.join(list)
    return int(num)

def calc(value):
    result = []
    while value:
        result.append(value % 10)
        value = value // 10
    #逆序，按正常的顺序返回
    result.reverse()
    return result

# a = Polynomial(5, [1,4,3,0,1])
# if a.is_irr():
#     print('不可约')
# else:
#     print('可约')

# with open('res.txt', 'w') as f:
#     sum = 0
#     for i in range(5):
#         a = [1]
#         a.insert(0,i)
#         for j in range(5):
#             a.insert(0,j)
#             for k in range(5):
#                 a.insert(0,k)
#                 for m in range(5):
#                     a.insert(0,m)
#                     c = a.copy()
#                     d = a.copy()
#                     d.reverse()
#                     b = Polynomial(5, c)
#                     if b.is_irr() :
#                          f.write(str(d)+'\n')
#                          sum = sum +1
#                     a.pop(0)
#                 a.pop(0)
#             a.pop(0)
#         a.pop(0)
#     a.pop(0)
#     f.write('----------------\n')
#     f.write('sum='+str(sum))

n = int(input("请输入你想要的多项式次数\n"))
start = pow(5,n)
end = start*2

time_start = time.time() #开始计时

with open('res.txt','w') as f:
    sum = 0
    for x in range(start,end):
        a = calc(tenToAny(5,x))
        b = a.copy()
        b.reverse()
        c = b.copy()
        poly = Polynomial(5, c)
        if poly.is_irr():
            f.write(str(a)+'\n')
            sum = sum +1
    f.write('-------------------\n')
    f.write('sum='+str(sum))
    print('-------------')
    print(sum)

time_end = time.time()    #结束计时
time_c= time_end - time_start   #运行所花时间
print('time cost', time_c, 's')