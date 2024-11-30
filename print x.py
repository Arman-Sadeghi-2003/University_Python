for i in range(1,9):
    for j in range(1,9):
        if j == 4 or i == 4:
            print('*',end=('\t'))
        else:
            print(' ',end=('\t'))
    print()

