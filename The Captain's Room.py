K=int(input()) # The size of each group
rooms=list(map(int,input().split()))  #the unordered elements of the room number list.

s1=set( )  #unique numbers of list
s2=set( )  #room number appearing more than one

for room in rooms:
    if room in s1:
        s2.add(room)
    else:
        s1.add(room)

s=s1.difference(s2)
print(*s)

"""my_list = [1, 2, 3, 4, 5]
print(*my_list)  # çıktı: 1 2 3 4 5"""
