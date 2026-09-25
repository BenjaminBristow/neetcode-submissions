class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # initialise all lists containing sets

        rowList = [set() for i in range(9)]
        collumnList = [set() for i in range(9)]
        squaresList = [set() for i in range(9)]

        # initialise square index
        squareIndexList = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]

        for row in range(9):
            for collumn in range(9):
                # for every num in every row in board
                num = board[row][collumn]

                # if empty, skip iteration
                if num == ".":
                    continue

                #check row
                if num in rowList[row]:
                    return False
                else:
                    rowList[row].add(num)

                #check collumn
                if num in collumnList[collumn]:
                    return False
                else:
                    collumnList[collumn].add(num)

                #check square

                # get square index
                squareIndex = squareIndexList[row//3][collumn//3]

                if num in squaresList[squareIndex]:
                    return False
                else:
                    squaresList[squareIndex].add(num)
        
        return True
