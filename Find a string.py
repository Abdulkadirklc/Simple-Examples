def count_substring(string, sub_string):
    m=0
    c=len(string)
    for i in range(0,c):
        if string[i:i+len(sub_string)] == sub_string:
            m+=1
         
    return m

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
