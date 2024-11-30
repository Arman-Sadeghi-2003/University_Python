for i in range(1, 9):
    for j in range(1, 9):
        if i == 4 or j == 4:
            print("*",end=('\t'))
        else:
            print(' ',end=('\t'))
    print()