tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printtable(x):

    colwidth = [0]*len(x)
    for i in range(len(x)):
        for j in range(len(x[i])):
            if len(x[i][j])> colwidth[i]:
                colwidth[i] = len(x[i][j])

    for a in range(len(x[0])):
        for b in range(len(x)):
            print(x[b][a].rjust(colwidth[b]), end = '')
        print('')

#easier and better solution : god level
tableData = [['apples', 'oranges', 'cherries', 'banana'],
                     ['Alice', 'Bob', 'Carol', 'David'],
                     ['dogs', 'cats', 'moose', 'goose']]




for a, b, c in zip(tableData[0], tableData[1], tableData[2]):
    print(a.rjust(10), b.rjust(10), c.rjust(10))





    #newList = list(zip(*x))

#    for r in range(len(x)):
#        for i in x[r]:
#            if len(i) > colwidth[r]:
#                colwidth[r]= len(i)
#    return colwidth
#    print('>>>>>')
#    print(newList)
#    for row in newList:
#        print(row[0].ljust(0))


#    new = [r for i in newList for r in i]
#    print(new)

#    colWid = [0]* len(x)
#    for i in x:
#        for j in i:
#            for k in range(len(x)):
#                if len(j)> colWid[k]:
#                    colWid[k]= len(j)



printtable(tableData)
    #newList = [[row[i] for row in list] for i in range(len(tableData))]

    #newRow = ([row[i] for row in newList for row[i] in row])
    #print(newRow)
