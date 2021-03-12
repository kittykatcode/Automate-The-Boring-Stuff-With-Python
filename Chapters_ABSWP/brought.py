allGuest = {'Alice' : {'apple': 5 , 'orange': 12},
            'bob' : {'sandwich' : 3, 'apple': 8},
            'Carol': {'cups': 14, 'pie': 20}}

def totalbrought(guest, item):
    brought = 0
    for k,v in guest.items():
        brought = brought + v.get(item,0)
    return brought

print('Number of things being tonight')
print(' - apple-   ' +str(totalbrought(allGuest, 'apple')))
print(' - Cups-    ' +str(totalbrought(allGuest, 'cups')))
print(' - Cake-    ' +str(totalbrought(allGuest, 'cake')))
print(' - sandwich-' +str(totalbrought(allGuest, 'sandwich')))
print(' - pie-     ' +str(totalbrought(allGuest, 'pie')))
