import tkinter as tk
from tkinter import messagebox


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    if all(cell != ' ' for row in board for cell in row):
        return 'Draw'
    return None


def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return -1
    elif winner == 'O':
        return 1
    elif winner == 'Draw':
        return 0
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score


def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move


def on_button_click(row, col):
    if board[row][col] == ' ' and not check_winner(board):
        board[row][col] = 'X'
        buttons[row][col].config(text='X')
        winner = check_winner(board)
        if winner:
            end_game(winner)
            return
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = 'O'
            buttons[move[0]][move[1]].config(text='O')
        winner = check_winner(board)
        if winner:
            end_game(winner)


def end_game(winner):
    if winner == 'Draw':
        messagebox.showinfo("TicTacToe", "It's a draw!")
    else:
        messagebox.showinfo("TicTacToe", f"The winner is {winner}!")
    root.quit()


board = [[' ' for _ in range(3)] for _ in range(3)]
root = tk.Tk()
root.title("TicTacToe")

buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=' ', font='normal 20 bold', height=2, width=5,
                                  command=lambda i=i, j=j: on_button_click(i, j))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()


