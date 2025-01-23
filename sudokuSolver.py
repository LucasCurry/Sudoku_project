#Opens the file where the sudoku to solve is taken from and
#the file where the solved sudoku is stored.
f = open('sudoku_pussel.csv', mode='r')
end_storage = open('solved.csv', mode='w')

#Sets a flag for when the sudoku is solved.
solution_found = False

ls = f.read().split('\n')
counter = 0
for i in ls:
    ls[counter] = i.split(',')
    counter += 1

#Converts all elements in list to ints
for i in range(len(ls)):
    for j in range(len(ls[i])):
        ls[i][j] = int(ls[i][j])


#Checks if n is found in y (column), then if
# it's found in x (row). Finally checks for n i blocks
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

#Recrusive function that looks for 0, uses the possible function to
#check which number n could be. When it find a number it adds it to the
#list and recalls the function. If all 0 are replaced it sets the
#solution_found flag to True and leaves function.
def solve():
    global ls
    global solution_found
    for y in range(9):
        for x in range(9):
            if ls[y][x] == 0:
                for n in range(1, 10):
                    if possible(y,x,n):
                        ls[y][x] = n
                        solve()
                        if solution_found:
                            return
                        ls[y][x] = 0
                return
    solution_found = True

#Function to print row
def row (ls, row_var):
    print(ls[row_var])

#Function to print column
def column (ls, row_var, column_var):
    print(ls[row_var][column_var])

#Function to print block
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

    #Code to choose specific square to check if a number n is possible in.
    '''yxn_temp = input('Choose a square to check, Choose row, column and what you want to enter with space inbetween: ')
    temp_list = yxn_temp.split()
    y = int(temp_list[0])-1
    x = int(temp_list[1])-1
    n = int(temp_list[2])'''


    solve()

    #Converts list back to string
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            ls[i][j] = str(ls[i][j])

    #Writes list to solved.csv
    for i in range(9):
        end_storage.write('\n')
        for j in range(9):
            end_storage.write(f'{ls[i][j]},')


    #Code to let user print out specific rows/columns/blocks
    '''row_var = int(input('Choose a sudoku row from 1-9 to print: '))-1
    column_var = int(input('Choose a sudoku column from 1-9 to print: '))-1
    block_var = int(input('Choose a sudoku block from 1-9 to print: '))

    row(ls, row_var)
    column(ls, row_var, column_var)
    blocks(ls, block_var)'''

    #Flavor code to let someone continue or end program
    print(ls)
    cont = input('Continue(y/n)\n')
    if(cont == 'n'):
        print('Alrighty tighty, goodbye!')
        break
f.close()
end_storage.close()
