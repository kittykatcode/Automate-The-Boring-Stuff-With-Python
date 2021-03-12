def PrintPicnic(iteamDict, leftWidth, rightWidth):
    print('Picnic Iteams'.center(leftWidth + rightWidth, '-'))
    for k,v in iteamDict.items():
        print(k.ljust(leftWidth,'.') +str(v).rjust(rightWidth, '*'))

PicnicItems = {'sandwhich':54, 'apples':23, 'cups': 42, 'cookies':78, 'yup': 'gogo'}
PrintPicnic(PicnicItems,12,5)
PrintPicnic(PicnicItems,20,8)
