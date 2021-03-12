#names = ['Java', 'Python', 'Go', 3]
#print('String: ' + (','.join(str(names))))

#for i in enumerate(names):
#    print(i)
#time = [1,2,3,4]

#newlist = enumerate(list(zip(names,time)))
#print(newlist)

#for a,b in newlist:
#    print(a,b)
tableData = [['apples', 'oranges', 'cherries', 'banana'],
                     ['Alice', 'Bob', 'Carol', 'David'],
                     ['dogs', 'cats', 'moose', 'goose']]




for a, b, c in zip(tableData[0], tableData[1], tableData[2]):
    print(a.rjust(10), b.rjust(10), c.rjust(10))
