number_grid=[
        [1,2,3],
        [4,4,6],
        [7,8,9],
        [0]
        ]
def print_each_grid(row,col):
    if(row>4 and col>3):
        print("maximum row is 2 and maximum coloum is 3")
    else:
        print(number_grid[row][col])

def print_row():
    for row in number_grid:
        print(row)

def print_col():
    for row in number_grid:
        for col in row:
            print(col)



input_row=input("insert row number: ")
input_coloum=input("insert coloum number: ")
print(print_each_grid(int(input_row),int(input_coloum)))

row=print_row()
print(row)

coloum=print_col()
print(coloum)

