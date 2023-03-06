def merge_the_tools(string, k):
    liste = []

    for i in range(0, len(string), k):
        liste.clear()
        liste.append(string[i:i + k])
        newo = ""
        for a in liste[0]:
            if a not in newo:
                newo += a
            else:
                continue

        print(newo)
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
