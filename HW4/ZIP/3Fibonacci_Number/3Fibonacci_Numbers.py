import argparse
parser = argparse.ArgumentParser()
parser.add_argument("n")
args = parser.parse_args()
n = int(args.n)
if n ==0:
    print('n is 0')
elif n==1:
        print('1')
else:      
    l=[1,1]
    for i in range(n-2):
        sum=l[-1]+l[-2]
        l.append(sum)
    print(l)