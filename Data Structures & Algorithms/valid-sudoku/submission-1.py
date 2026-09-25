class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # initialise all lists containing sets
        rows = set()
        collumns = set()
        squares = set()

        # initialise square index
        squareIndex = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]

        for row in range(9):
            for collumn in range(9):
                num = board[row][collumn]

                if num == ".":
                    continue

                # rows
                rNum = (row, num)
                if rNum in rows:
                    return False
                else:
                    rows.add(rNum)

                # collumns
                cNum = (collumn, num)
                if cNum in collumns:
                    return False
                else:
                    collumns.add(cNum)

                # squares
                square = squareIndex[row//3][collumn//3]
                
                sNum = (square, num)
                if sNum in squares:
                    return False
                else:
                    squares.add(sNum)
        
        return True
                

