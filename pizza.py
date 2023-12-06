"""
Name of the Team:Dary

Team members:
1. Danylo Bezruchenko
2. Mariia Svimonishvili
"""

#our solution 
def pizza(filename):
    likes = []
    dislikes = []
    file = open(filename, 'r')
    linenum = int(file.readline())

    for i in range(linenum*2):
        if i % 2 == 0:
            likes.extend(file.readline()[2:-1].split(' '))
        if i % 2 != 0:
            dislikes.extend(file.readline()[2:-1].split(' '))\
            
    uniqlik = []
    uniqdis = []
    for i in likes:
        if i in uniqlik:
            continue
        else:
            uniqlik.append(i)
    for j in dislikes:
        if j in uniqdis:
            continue
        else:
            uniqdis.append(j)
    for i in uniqlik:
        if i in uniqdis:
            uniqlik.remove(i)
    file.close()
    f = open('solution_e.txt',"w")
    f.write(str(len(uniqlik)))
    for i in uniqlik:
        f.write(' '+i)
    f.close()

pizza('input_e.txt')
