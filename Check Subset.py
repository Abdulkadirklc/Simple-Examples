"""You are given two sets A,  and B .
Your job is to find whether set  is A a subset of set B .

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

Input Format

The first line will contain the number of test cases, T.
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space separated elements of set A.
The third line of each test case contains the number of elements in set B.
The fourth line of each test case contains the space separated elements of set B."""


T=int(input())
for i in range(T):
    A=int(input())
    A_set= set(map(int,input().split()))
    B=int(input())
    B_set= set(map(int,input().split()))
    Its= len(A_set.intersection(B_set))
    if Its==A:
        print("True")
    else:
        print("False")
