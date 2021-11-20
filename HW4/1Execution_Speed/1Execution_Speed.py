import time #import time package
#begining of part a
t=time.perf_counter()
N=10000000
for i in range (N):
    pass
t0=time.perf_counter()
print('The average of pass statement:',(t0-t)/N)
#begining of part b
t1=time.perf_counter()
N=10000000
for i in range (N):
    float(3.1415926535768)+float(6.62607015*10**-34)
t2=time.perf_counter()
print('The average of addition of two float variables:',(t2-t1)/N)
#begining of part c
t3=time.perf_counter()
N=10000000
for i in range (N):
    float(3.1415926535768)*float(6.62607015*10**-34)
t4=time.perf_counter()
print('The average of multiplication of two float variables:',(t4-t3)/N)
#begining of part d
t5=time.perf_counter()
N=10000000
for i in range (N):
    float(3.1415926535768)/float(6.62607015*10**-34)
t6=time.perf_counter()
print('The average of division of two float variables:',(t6-t5)/N)
#begining of part e
t7=time.perf_counter()
N=10000000
for i in range (N):
    int(3.1415926535768)/int(6.62607015)
t8=time.perf_counter()
print('The average of division of two integer variables:',(t8-t7)/N)
#begining of part f one number
mylist=[]
t9=time.perf_counter()
N=10000000
for i in range (N):
    mylist.append(8)
t10=time.perf_counter()
print('The average of appending one number to a list:',(t10-t9)/N)
#begining of part f long list
mylist=[]
t15=time.perf_counter()
N=10000000
for i in range (N):
    mylist=range(10**7)
t16=time.perf_counter()
print('The average of appending a long list:',(t16-t15)/N)
#begining of part g
t11=time.perf_counter()
N=10000000
def nothing():
    pass
for i in range (N):
    nothing()
t12=time.perf_counter()
print('The average of call a function that does nothing:',(t12-t11)/N)
#begining of part h
t13=time.perf_counter()
N=10000000
def fadd():
    float(3.1415926535768)+float(6.62607015*10**-34)
for i in range (N):
    fadd()
t14=time.perf_counter()
print('The average of call to a function that add two float variables:',(t14-t13)/N)