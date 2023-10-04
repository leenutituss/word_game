def find_word(board, word):
    def is_valid(x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])

    def search(x, y, index):
        if index == len(word):
            return True

        if not is_valid(x, y) or board[x][y] != word[index]:
            return False

        original_char = board[x][y]
        board[x][y] = "#" 

       
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]

        for i in range(8):
            if search(x + dx[i], y + dy[i], index + 1):
                board[x][y] = original_char  
                return True

        board[x][y] = original_char  
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if search(i, j, 0):
                return True

    return False

