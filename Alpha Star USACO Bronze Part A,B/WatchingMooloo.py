#print(d)
#res=0
#s=False
#for x in range(N):
#    if s==False:
#        res+=K+1
#        s=True
#        
#    elif s:
#        if d[x]-d[x-1]+1<=2*K+2:
#            res+=d[x]-d[x-1]
#        else:
#            
#            s=False
#print(res)
#
#
#
#a = []




N, K = map(int, input().split())
d = list(map(int, input().split()))
res=0
for x in range(N):
    if x==0: #checking for first day
        res+=K+1
    else:
        p=d[x]-d[x-1]
        l=K+1
        res+=min(p,l)
print(res)




















#counter = 0
#subscription = False
#for i in range(N-1):
#    test1 = d[i+1]-d[i]+1+K
#    if subscription == False:
#        test2 = 2*K+2
#    else:
#        test2 = 1+K
#    #print(test1, test2)
#    if test2 <= test1:
#        counter += test2
#        subscription = True
#    else:
#        counter += test1
#        subscription = False
#print(counter)






#res=0
#import sys
#i=1
#
#ib=False
#while i<N+1:
#    if d[i]-d[i-1]+1<=K+1 and ib:
#        res+=d[i]-d[i-1]+1
#    elif d[i]-d[i-1]+1<=K+1 and ib==False:
#        res+=d[i]-d[i-1]+1+K
#    else:
#       res+=K+1
#       ib=False
#    i+=1
#print(res)
