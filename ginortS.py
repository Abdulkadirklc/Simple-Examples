"""You are given a string S.
Your task is to sort the string S in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits."""

S=sorted(input())
Lower=[]
Upper=[]
Odd=[]
Even=[]

for i in S:
    if i.islower():
        Lower.append(i)
    if i.isupper():
        Upper.append(i)
    if i.isdigit():
        i=int(i)
        if i%2==0:
            Even.append(i)
        if i%2==1:
            Odd.append(i)
Sortedlist="".join(map(str,Lower+Upper+Odd+Even))
print(Sortedlist)
