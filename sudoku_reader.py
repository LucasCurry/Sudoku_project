f = open('sudoku/sudoku_pussel.csv', mode='r') 

ls = f.read().split('\n')
counter = 0
for i in ls:
    #print(type(i))
    ls[counter] = i.split(',')
    counter += 1
    #print(type(ls[counter]))

def row (ls, row_var):
    print(ls[row_var])
    
def column (ls, row_var, column_var):
    print(ls[row_var][column_var])

def squares (ls, sqaure_var):
    if (sqaure_var == 1):
        print(f'{ls[0][0:3]}\n{ls[1][0:3]}\n{ls[2][0:3]}')
    elif (square_var == 2):
        print(f'{ls[0][3:6]}\n{ls[1][3:6]}\n{ls[2][3:6]}')
    elif (square_var == 3):
        print(f'{ls[0][6:9]}\n{ls[1][6:9]}\n{ls[2][6:9]}')
    elif (square_var == 4):
        print(f'{ls[3][0:3]}\n{ls[4][0:3]}\n{ls[5][0:3]}')
    elif (square_var == 5):
        print(f'{ls[3][3:6]}\n{ls[4][3:6]}\n{ls[5][3:6]}')
    elif (square_var == 6):
        print(f'{ls[3][6:9]}\n{ls[4][6:9]}\n{ls[5][6:9]}')
    elif (square_var == 7):
        print(f'{ls[6][0:3]}\n{ls[7][0:3]}\n{ls[8][0:3]}')
    elif (square_var == 8):
        print(f'{ls[6][3:6]}\n{ls[7][3:6]}\n{ls[8][3:6]}')
    elif (square_var == 9):
        print(f'{ls[6][6:9]}\n{ls[7][6:9]}\n{ls[8][6:9]}')




while(True):
    #row_var = int(input('Choose a sudoku row from 1-9 to print: '))-1
    #column_var = int(input('Choose a sudoku column from 1-9 to print: '))-1
    square_var = int(input('Choose a sudoku square from 1-9 to print: '))

    #row(ls, row_var)
    #column(ls, row_var, column_var)
    squares(ls, square_var)

        
    cont = input('Continue(y/n)\n')
    if(cont == 'n'):
        print('Alrighty tighty, goodbye!')
        break
f.close()