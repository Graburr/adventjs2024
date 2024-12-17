from typing import List, Literal

def move_train(board: List[str], mov: Literal['U', 'D', 'R', 'L']
               ) -> Literal['none', 'crash', 'eat']:
    for i, row in enumerate(board):
        if '@' in row:
            head_x, head_y = i, row.index('@')
            break

    moves = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    dx, dy = moves[mov]
    new_x, new_y = head_x + dx, head_y + dy

    if not (0 <= new_x < len(board)) or not (0 <= new_y < len(board[0])):
        return "crash"

    target = board[new_x][new_y]
    if target == 'o':
        return "crash"
    elif target == '*':
        return "eat"
    else:
        return "none"