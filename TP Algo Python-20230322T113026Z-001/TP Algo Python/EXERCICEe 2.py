A=input("Entrez la phrase :")
C=[] 
B=[]
for i in A:
    C+=i
for i in range(len(C)-1):
    if C[i]==" " and C[i+1]==" ":
        continue
    elif C[0]==" ":
        B.append(C[i+1])
    else:
        B.append(C[i])

for i in B:
    print(end=f"{i}")
    

                 