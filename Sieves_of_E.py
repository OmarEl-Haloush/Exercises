import time
T1=time.perf_counter()
N=input('Compute all Prime numbers <N\nN= ')
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
fout=open('prime.dat','w')
i=0
#while string[i]<=len(string):
 #   fout.write(str(string[i]))
for i in string:
    fout.write(str(i))
    fout.write('\n')
 
fout.close()
T2=time.perf_counter()
print('Time required to find',len(string),'in',T2-T1,'sec.')