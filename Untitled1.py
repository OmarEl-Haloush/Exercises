import time
import sys
# sys.argv is a list with the command-line arguments. sysv.arg[0] is the name of Python script
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
T1=time.perf_counter()
N=sys.argv[1]
file=sys.argv[2]
print(N)
n=int(N)

print(type(n),n)
string=[]
x=2
while x <=n:
    string.append(x)
    x+=1
print(string)
for i in string:
    j=i
    while i in string:
        if i*j<=n:
            p=i*j
            
            if p in string:
                string.remove(p)
                
            j+=1
        else:
            i+=1
print(string)
fout=open(sys.argv[2],'w')
i=0
for i in string:
    fout.write(str(i))
    fout.write('\n')
 
fout.close()
T2=time.perf_counter()
print('Time required to find',len(string),'in',T2-T1,'sec.')