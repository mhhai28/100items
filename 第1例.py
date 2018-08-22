a = [1,2,3,4]
t=0
for i in a:
    for j in a:
        for k in a:
            if((i!=j)and(i!=k)and(j!=k)):
                t=t+1;
                print(i,j,k)
print(t)
