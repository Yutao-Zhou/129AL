import os
import time
c=0
while c<10:
    c=c+1
    print(c)
    time.sleep(0.5)
    if c%10==0:
        print('I am about to fork!')
        retval = os.fork()
        child = (retval == 0)       
        if child:
            print('I am about to execute ls:')
            os.execv("/bin/ls", ["ls", "-l"])