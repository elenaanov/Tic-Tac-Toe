t = '_' * 9

print(f'''---------
| {t[0]} {t[1]} {t[2]} |
| {t[3]} {t[4]} {t[5]} |
| {t[6]} {t[7]} {t[8]} |
---------''')

move_numb = 0

while True:

    move_numb += 1

    # new move
    check = False
    ind = 0

    while check is False:
        row_col = input()
        print(f'Enter the coordinates: {row_col}')
        check = True

        row, col = row_col.split()
        ind = (((int(row) - 1) * 3) + (int(col) + 2)) - 3

        if row.isnumeric() is False or col.isnumeric() is False:
            print('You should enter numbers!')
            check = False
        elif row not in ['1', '2', '3'] or col not in ['1', '2', '3']:
            print('Coordinates should be from 1 to 3!')
            check = False
        elif t[ind] != '_':
            print('This cell is occupied! Choose another one!')
            check = False

    # print new grid
    if move_numb % 2 == 1:
        t = t[:ind] + 'X' + t[ind + 1:]
    else:
        t = t[:ind] + 'O' + t[ind + 1:]

    print(f'''---------
    | {t[0]} {t[1]} {t[2]} |
    | {t[3]} {t[4]} {t[5]} |
    | {t[6]} {t[7]} {t[8]} |
    ---------''')

    # check the victory
    num_x = t.count('X')
    num_o = t.count('O')
    num_empty = t.count('_')

    win = [[1, 1, 1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 1, 1],
           [1, 0, 0, 1, 0, 0, 1, 0, 0],
           [0, 1, 0, 0, 1, 0, 0, 1, 0],
           [0, 0, 1, 0, 0, 1, 0, 0, 1],
           [1, 0, 0, 0, 1, 0, 0, 0, 1],
           [0, 0, 1, 0, 1, 0, 1, 0, 0]]

    t_matrix = [t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8]]

    t_bool_x = [1 if x == 'X' else 0 for x in t_matrix]
    t_bool_o = [1 if x == 'O' else 0 for x in t_matrix]

    win_x = 0
    win_o = 0

    for i in range(len(win)):
        check_x = [0] * 9
        check_o = [0] * 9

        for j in range(len(t_matrix)):
            if t_bool_x[j] == 1 and win[i][j] == 1:
                check_x[j] = 1
            if t_bool_o[j] == 1 and win[i][j] == 1:
                check_o[j] = 1

        if check_x == win[i]:
            win_x += 1
        if check_o == win[i]:
            win_o += 1

    if abs(num_x - num_o) >= 2 or win_x + win_o > 1:
        print('Impossible')
        break
    elif win_x + win_o == 0 and num_empty > 0:
        print('Game not finished')
    elif win_x + win_o == 0 and num_empty == 0:
        print('Draw')
        break
    elif win_x == 1:
        print('X wins')
        break
    elif win_o == 1:
        print('O wins')
        break
