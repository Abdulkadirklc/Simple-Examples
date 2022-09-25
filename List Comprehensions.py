if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l=list()
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                if i+j+k!=n:
                    l.append([i,j,k])
    print(l)                
    
    """It gives us a list of number which is its sum not equal to n """
