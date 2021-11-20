#part a
# When I use 'python3 -i' to 'import os' and run:'os.execv("/bin/ls", ["ls", "-l"])', it will return the
# same 'ls -l' result in the current directory. It will quit python and return to Linux at the same time.
# This is interesting becaue usually program would stay in python after the program terminate.
# This program is special becuase os.execv made it exit python when the program terminate.
# 'fork' creat parallel process and continue running both the parten program and the child program.
# 'execv' is replacing the initial program with ls -l. (in part b it replace child program with ls -l and then terminate it)
# This is why it return to the parent program, which is counting in part b, after it give the ls -l.
# Also, this is why we have finite thread and don't end up crashing the system.
# The difference is fork great a copy of the current program, where execv replace the current program.

#part b
import os
import time
c=0
while True:
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