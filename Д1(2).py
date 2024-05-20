

table = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

def draw_board(board) :
    for row in board :
        for cell in row :
            print(cell, end=' ')
        print()

def winner(board, player) :
    for row in board :
        if row.count(player) == 3 :
            return True
        
    for i in range(3) :
        if board[0][i] == player and board[1][i] == player and board[2][2] == player :
            return True

    if board[0][0] == player and board[1][1] == player and board[2][0] == player :
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player :
        return True
    
current_player = 'X'

while True :
    draw_board(table)
    print('Ход игрока: ', current_player)
    row = int(input('Введите номер строки: ')) - 1
    col = int(input('Введите номер столбца: ')) - 1

    if table[row][col] != '-' :
        print('Ячейка занята')
        continue
    
    table[row][col] = current_player

    if winner(table, current_player) :
        draw_board(table)
        print('Игрок ' + current_player + ' выиграл')
        break
    current_player = '0' if current_player == 'X' else 'X'





    
