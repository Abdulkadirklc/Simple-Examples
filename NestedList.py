'''Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.'''

if __name__ == '__main__':
    records=[]
    scores=[]
    for x in range(int(input())):
        name = str(input())
        score = float(input())
        records.append([name,score]) 
        scores.append(score)
    scores=sorted(set(scores))
    slgrade=scores[1]
    names=[]
    for x in records:
        if x[1]==slgrade:
            names.append(x[0])
    names.sort()
    for y in names:
        print(y)      
