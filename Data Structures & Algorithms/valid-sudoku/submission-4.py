class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            duplicate = set()
            for number in row:
                if number in duplicate and number != ".":
                    return False
                else:
                    duplicate.add(number)
        
        for x in range(len(board)):  
            duplicate = set()
            for y in range(len(board)):
                if board[y][x] in duplicate and board[y][x] != ".":
                    return False
                else:
                    duplicate.add(board[y][x])
        
        x = 0
        y = 0

        while x<=8:
            while y<=8:
                duplicate = set()
                duplicate.add(board[x][y])
                if board[x+1][y] in duplicate and board[x+1][y] != ".":
                    return False
                else:
                    duplicate.add(board[x+1][y])                
                if board[x+2][y] in duplicate and board[x+2][y] != ".":
                    return False
                else:
                    duplicate.add(board[x+2][y])
                if board[x][y+1] in duplicate and board[x][y+1] != ".":
                    return False
                else:
                    duplicate.add(board[x][y+1])
                if board[x][y+2] in duplicate and board[x][y+2] != ".":
                    return False
                else:
                    duplicate.add(board[x][y+2])
                if board[x+1][y+1] in duplicate and board[x+1][y+1] != ".":
                    return False
                else:
                    duplicate.add(board[x+1][y+1])
                if board[x+2][y+1] in duplicate and board[x+2][y+1] != ".":
                    return False
                else:
                    duplicate.add(board[x+2][y+1])
                if board[x+1][y+2] in duplicate and board[x+1][y+2] != ".":
                    return False
                else:
                    duplicate.add(board[x+1][y+2])
                if board[x+2][y+2] in duplicate and board[x+2][y+2] != ".":
                    return False
                else:
                    duplicate.add(board[x+2][y+2])
                y+=3
            x+=3

        return True
            
            
        