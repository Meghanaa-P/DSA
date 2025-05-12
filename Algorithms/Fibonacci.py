# using loop

prev2=0
prev1=1
print(prev2)
print(prev1)
for fibo in range(18):
    newFibo=prev2+prev1
    print(newFibo)
    prev2=prev1
    prev1=newFibo

#using recurrsion

print(0)
print(1)
count = 2
def fibbo(pre1,pre2):
    global count
    if count<=19:
        newFib=pre1+pre2
        print(newFib)
        pre2=pre1
        pre1=newFib
        count += 1
        fibbo(pre1,pre2)
    else:
        return
fibbo(1,0)

#taking input finding fibonacci for nth number

def F(n):
    if n<=1:
        return 1
    else:
        return F(n-1)+F(n-2)

n=int(input("Enter the number = "))
print(F(n))



