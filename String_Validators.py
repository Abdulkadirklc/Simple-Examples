s = input()
print(any([a.isalnum() for a in s])) 
#This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
print(any([a.isalpha() for a in s]))
#This method checks if all the characters of a string are alphabetical (a-z and A-Z).
print(any([a.isdigit() for a in s]))
#This method checks if all the characters of a string are digits (0-9).
print(any([a.islower() for a in s]))
#This method checks if all the characters of a string are lowercase characters (a-z).
print(any([a.isupper() for a in s]))
#This method checks if all the characters of a string are uppercase characters (A-Z).

#any() => returns True if any item in an iterable are true, otherwise it returns False.If the iterable object is empty, the any() function will return False.
