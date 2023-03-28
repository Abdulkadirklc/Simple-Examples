def print_formatted(number):
    w = len((bin(number))[2:])
    for i in range(1,number+1):
        decimal = i
        octal = oct(i)
        hexadecimal = hex(i)
        binary = bin(i)
        
        print(str(decimal).rjust(w," ") , str(octal[2:]).rjust(w," ") , str(hexadecimal[2:]).upper().rjust(w," ") , str(binary[2:]).rjust(w," "))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
