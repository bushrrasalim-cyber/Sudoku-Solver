board = [
   ["5","3",".",".","7",".",".",".","."],
   ["6",".",".","1","9","5",".",".","."],
   [".","9","8",".",".",".",".","6","."],
   ["8",".",".",".","6",".",".",".","3"],
   ["4",".",".","8",".","3",".",".","1"],
   ["7",".",".",".","2",".",".",".","6"],
   [".","6",".",".",".",".","2","8","."],
   [".",".",".","4","1","9",".",".","5"],
   [".",".",".",".","8",".",".","7","9"]

]
class Solution:
    def valid(self,row,col,num):
        box = (row//3)*3 + (col//3)
        if num in self.rows[row]:
            return False
        if num in self.cols[col]:
            return False
        if num in self.boxes[box]:
            return False
        return True
    def rec(self,board):
        best_row = -1
        best_col = -1
        best_num = None
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    possible = []

                    for num in "123456789":
                        if self.valid(row,col,num):
                            possible.append(num)
                    if best_num is None or len(possible)< len(best_num):
                        best_row = row
                        best_col = col
                        best_num = possible
                    if len(best_num) == 1:
                        break
            if best_num is not None and len(best_num) == 1:
                break
        if best_num is None:
            return True
        if len(best_num) == 0:
            return False
        row = best_row
        col = best_col
        for num in best_num:
            board[row][col] = num
            box = (row//3)*3 + (col//3)
            self.rows[row].add(num)
            self.cols[col].add(num)
            self.boxes[box].add(num)
            if self.rec(board):
                return True
            self.rows[row].remove(num)           
            self.cols[col].remove(num)
            self.boxes[box].remove(num)
            board[row][col] = "."
        return False
    def solveSudoku(self, board):
        self.rows = [set() for _ in range(9)]
        self.cols = [set()for _ in range(9)]
        self.boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    num = board[row][col]

                    box = (row // 3 ) * 3 + col // 3
                    self.rows[row].add (num)
                    self.cols[col].add (num)
                    self.boxes[box].add (num)


        self.rec(board)

if __name__ == "__main__":
    solution = Solution()
    solution.solveSudoku(board)
    print(board)
