def table(cells):
    print("---------")
    print("|", cells_listed[0], cells_listed[1], cells_listed[2], "|")
    print("|", cells_listed[3], cells_listed[4], cells_listed[5], "|")
    print("|", cells_listed[6], cells_listed[7], cells_listed[8], "|")
    print("---------")

cells = "         "
cells_listed = list(cells)
table(cells)
board = [
    [cells_listed[6], cells_listed[7], cells_listed[8]],
    [cells_listed[3], cells_listed[4], cells_listed[5]],
    [cells_listed[0], cells_listed[1], cells_listed[2]]
]
mark = 'X'

while True:
    coords = input('Enter the coordinates: ').split()
    if coords[0].isalpha() or coords[1].isalpha():
        print("You should enter numbers!")
    elif int(coords[0]) < 1 or int(coords[0]) > 3 or int(coords[1]) < 1 or int(coords[1]) > 3:
        print("Coordinates should be from 1 to 3!")
    else:
        if int(coords[0]) == 1 and int(coords[1]) == 1:
            if cells_listed[6] == ' ':
                cells_listed[6] = mark
                if mark == 'X':
                    mark = 'O'
                elif mark == 'O':
                    mark = 'X'
            else:
                print('This cell is occupied! Choose another one!')
        if int(coords[0]) == 1 and int(coords[1]) == 2:
            if cells_listed[3] == ' ':
                cells_listed[3] = mark
                if mark == 'X':
                    mark = 'O'
                elif mark == 'O':
                    mark = 'X'
            else:
                print('This cell is occupied! Choose another one!')
        if int(coords[0]) == 1 and int(coords[1]) == 3:
            if cells_listed[0] == ' ':
                cells_listed[0] = mark
                if mark == 'X':
                    mark = 'O'
                elif mark == 'O':
                    mark = 'X'
            else:
                print('This cell is occupied! Choose another one!')
        if int(coords[0]) == 2 and int(coords[1]) == 1:
            if cells_listed[7] == ' ':
                cells_listed[7] = mark
                if mark == 'X':
                    mark = 'O'
                elif mark == 'O':
                    mark = 'X'
            else:
                print('This cell is occupied! Choose another one!')
        if int(coords[0]) == 2 and int(coords[1]) == 2:
            if cells_listed[4] == ' ':
                cells_listed[4] = mark
                if mark == 'X':
                    mark = 'O'
                elif mark == 'O':
                    mark = 'X'
            else:
                print('This cell is occupied! Choose another one!')
        if int(coords[0]) == 2 and int(coords[1]) == 3:
            if cells_listed[1] == ' ':
                cells_listed[1] = mark
                if mark == 'X':
                    mark = 'O'
                elif mark == 'O':
                    mark = 'X'
            else:
                print('This cell is occupied! Choose another one!')
        if int(coords[0]) == 3 and int(coords[1]) == 1:
            if cells_listed[8] == ' ':
                cells_listed[8] = mark
                if mark == 'X':
                    mark = 'O'
                elif mark == 'O':
                    mark = 'X'
            else:
                print('This cell is occupied! Choose another one!')
        if int(coords[0]) == 3 and int(coords[1]) == 2:
            if cells_listed[5] == ' ':
                cells_listed[5] = mark
                if mark == 'X':
                    mark = 'O'
                elif mark == 'O':
                    mark = 'X'
            else:
                print('This cell is occupied! Choose another one!')
        if int(coords[0]) == 3 and int(coords[1]) == 3:
            if cells_listed[2] == ' ':
                cells_listed[2] = mark
                if mark == 'X':
                    mark = 'O'
                elif mark == 'O':
                    mark = 'X'
            else:
                print('This cell is occupied! Choose another one!')
        three_x_in_row = False
        three_o_in_row = False
        if cells_listed[0] == 'X' and cells_listed[1] == 'X' and cells_listed[2] == 'X':
            three_x_in_row = True
            break
        if cells_listed[3] == 'X' and cells_listed[4] == 'X' and cells_listed[5] == 'X':
            three_x_in_row = True
            break
        if cells_listed[6] == 'X' and cells_listed[7] == 'X' and cells_listed[8] == 'X':
            three_x_in_row = True
            break
        if cells_listed[0] == 'X' and cells_listed[3] == 'X' and cells_listed[6] == 'X':
            three_x_in_row = True
            break
        if cells_listed[1] == 'X' and cells_listed[4] == 'X' and cells_listed[7] == 'X':
            three_x_in_row = True
            break
        if cells_listed[2] == 'X' and cells_listed[5] == 'X' and cells_listed[8] == 'X':
            three_x_in_row = True
            break
        if cells_listed[0] == 'X' and cells_listed[4] == 'X' and cells_listed[8] == 'X':
            three_x_in_row = True
            break
        if cells_listed[2] == 'X' and cells_listed[4] == 'X' and cells_listed[6] == 'X':
            three_x_in_row = True
            break
        if cells_listed[0] == 'O' and cells_listed[1] == 'O' and cells_listed[2] == 'O':
            three_o_in_row = True
            break
        if cells_listed[3] == 'O' and cells_listed[4] == 'O' and cells_listed[5] == 'O':
            three_o_in_row = True
            break
        if cells_listed[6] == 'O' and cells_listed[7] == 'O' and cells_listed[8] == 'O':
            three_o_in_row = True
            break
        if cells_listed[0] == 'O' and cells_listed[3] == 'O' and cells_listed[6] == 'O':
            three_o_in_row = True
            break
        if cells_listed[1] == 'O' and cells_listed[4] == 'O' and cells_listed[7] == 'O':
            three_o_in_row = True
            break
        if cells_listed[2] == 'O' and cells_listed[5] == 'O' and cells_listed[8] == 'O':
            three_o_in_row = True
            break
        if cells_listed[0] == 'O' and cells_listed[4] == 'O' and cells_listed[8] == 'O':
            three_o_in_row = True
            break
        if cells_listed[2] == 'O' and cells_listed[4] == 'O' and cells_listed[6] == 'O':
            three_o_in_row = True
            break
        table(cells)

if three_x_in_row:
    output = 'X wins'
elif three_o_in_row:
    output = 'O wins'
else:
    output = 'Draw'
table(cells)
print(output)