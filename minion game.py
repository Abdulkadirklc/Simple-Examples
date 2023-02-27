def minion_game(string):
    string=s
    vov,con=0,0
    for i in range(len(s)):
        if (string[i] in 'AEIOU'):
            vov+=len(s)-i
        else:
            con+=len(s)-i
    if (vov>con):
        print(f"Kevin {vov}")
    elif (con>vov) :
        print(f'Stuart {con}')
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)
