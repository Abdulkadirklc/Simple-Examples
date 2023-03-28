liste = input().split()
n = int(liste[0])         # row     =>must be odd number
m = int(liste[1])         # column  =>should be equal to 3m

# upper pattern
for i in range(0,n//2):
    print("-"*((m//2)-1-3*i )+".|."*(2*i+1) +"-"*((m//2)-1-3*i))
    
print("-"*((m//2)-3)+"WELCOME"+"-"*((m//2)-3))

# lower pattern
i = 0
for l in range(n//2,0,-1):
    print("-"*3*(i+1)+".|."*(2*(l-1)+1) +"-"*3*(i+1))
    i += 1
    
    
################## 2.Way ##############################

m,n = map(int,input().split())

for i in range(1,m,2):
    print((".|."* i).center(n,"-"))

print("WELCOME".center(n,"-"))

for i in range(m,1,-2):
    print((".|."* (i-2)).center(n,"-"))
