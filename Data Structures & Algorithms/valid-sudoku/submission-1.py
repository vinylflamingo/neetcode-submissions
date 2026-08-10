class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        if not self.isValidRow(board):
            return False

        if not self.isValidColumn(board):
            return False

        if not self.isValidSection(board):
            return False

        return True
                    
                
    def isValidRow(self, board: List[List[str]]) -> bool:
        for row in board:
            row_array = [0] * len(board)
            #check rows 
            for i in row:
                if i == ".":
                    continue
                else: 
                    if row_array[int(i) - 1] > 0:
                        return False # we found a duplicate number in the row
                    else: 
                        row_array[int(i) - 1] += 1
        return True

    def isValidColumn(self, board: List[List[str]]) -> bool:
        current_col = 0

        while current_col < len(board):
            col_map = [0] * len(board)
            for row in board:
                cell = row[current_col]
                if cell == ".":
                    continue

                if col_map[int(cell) - 1] > 0:
                    return False
                else: 
                    col_map[int(cell) - 1] += 1
            current_col += 1
        
        return True
            
    def isValidSection(self, board: List[List[str]]) -> bool:
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                collection = [0] * 9

                for dr in range(3):
                    for dc in range(3):
                        cell = board[r + dr][c + dc]

                        if cell == ".":
                            continue

                        idx = int(cell) - 1
                        if collection[idx] > 0:
                            return False
                        collection[idx] += 1

        return True 





        