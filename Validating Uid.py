"""ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0-9).
It should only contain alphanumeric characters (a-z, A-Z & 0-9).
No character should repeat.
There must be exactly 10 characters in a valid UID."""



n=int(input())
for z in range(n):
    uid=str(input())
    t=0
    c=0
    b=0
    for a in uid:
        for y in uid:
            if a==y:
                t+=1
    if len(uid)==10 and t==10:
        for i in uid:
            if i.isupper()==True:
                c+=1
            if i.isnumeric()==True:
                b+=1
        if b>=3 and c>=2 and uid.isalnum()==True:
            print("Valid")
        else:
            print("Invalid")   
    else:
        print("Invalid")           
   
