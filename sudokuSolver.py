f = open('sudoku_pussel.csv', mode='r')

ls = f.read().split('\n')
counter = 0
for i in ls:
    ls[counter] = i.split(',')
    counter += 1

for i in range(len(ls)):
    for j in range(len(ls[i])):
        ls[i][j] = int(ls[i][j])


def possible(y,x,n):
    global ls
    for i in range(9):
        if ls[y][i] == n:
            return False
    for i in range(9):
        if ls[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if ls[y0+i][x0+j] == n:
                return False
    return True

def solve():
    global ls
    for y in range(9):
        for x in range(9):
            if ls[y][x] == 0:
                for n in range(1, 10):
                    if possible(y,x,n):
                        ls[y][x] = n
                        solve()
                        ls[y][x] = 0
                return
    end_storage = open('solved.csv', mode='w')
    for i in range(9):
        for j in range (9):
            end_storage.write(ls[i][j])
    print(ls)


def row (ls, row_var):
    print(ls[row_var])
def column (ls, row_var, column_var):
    print(ls[row_var][column_var])

def blocks (ls, block_var):
    if (block_var == 1):
        print(f'{ls[0][0:3]}\n{ls[1][0:3]}\n{ls[2][0:3]}')
    elif (block_var == 2):
        print(f'{ls[0][3:6]}\n{ls[1][3:6]}\n{ls[2][3:6]}')
    elif (block_var == 3):
        print(f'{ls[0][6:9]}\n{ls[1][6:9]}\n{ls[2][6:9]}')
    elif (block_var == 4):
        print(f'{ls[3][0:3]}\n{ls[4][0:3]}\n{ls[5][0:3]}')
    elif (block_var == 5):
        print(f'{ls[3][3:6]}\n{ls[4][3:6]}\n{ls[5][3:6]}')
    elif (block_var == 6):
        print(f'{ls[3][6:9]}\n{ls[4][6:9]}\n{ls[5][6:9]}')
    elif (block_var == 7):
        print(f'{ls[6][0:3]}\n{ls[7][0:3]}\n{ls[8][0:3]}')
    elif (block_var == 8):
        print(f'{ls[6][3:6]}\n{ls[7][3:6]}\n{ls[8][3:6]}')
    elif (block_var == 9):
        print(f'{ls[6][6:9]}\n{ls[7][6:9]}\n{ls[8][6:9]}')




while(True):


    '''yxn_temp = input('Choose a square to check, Choose row, column and what you want to enter with space inbetween: ')
    temp_list = yxn_temp.split()
    y = int(temp_list[0])-1
    x = int(temp_list[1])-1
    n = int(temp_list[2])'''


    solve()
    row_var = int(input('Choose a sudoku row from 1-9 to print: '))-1
    column_var = int(input('Choose a sudoku column from 1-9 to print: '))-1
    block_var = int(input('Choose a sudoku block from 1-9 to print: '))

    row(ls, row_var)
    column(ls, row_var, column_var)
    blocks(ls, block_var)

    cont = input('Continue(y/n)\n')
    if(cont == 'n'):
        print('Alrighty tighty, goodbye!')
        break
f.close()