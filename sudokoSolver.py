def checkRow(possibleSolution):
    checkedList = []
    for i in range(9):
        if sorted(possibleSolution[i]) == list(range(1, 10)):
            checkedList.append(0)
        else:
            checkedList.append(1)
    return sum(checkedList)
def checkColumn(possibleSolution):
    count = 0
    newList = []
    columList = []
    checkedList = []
    for i in range(9):
        for q in range(9):
           newList.append(possibleSolution[q][i])
    while count<len(newList):
        columList.append(newList[count:count+9])
        count += 9
    for i in range(9):
        if sorted(possibleSolution[i]) == list(range(1, 10)):
            checkedList.append(0)
        else:
            checkedList.append(1) 
    return sum(checkedList)
def check3x3(possibleSolution):
    answerList = []
    checkedList = []
    for row in range(3):
        for column in range(3):
            threeBythree = []
            for i in range(3):
                for j in range(3):
                    threeBythree.append(possibleSolution[3*row+i][3*column+j])
            answerList.append(threeBythree)
    for i in range(9):
        if sorted(possibleSolution[i]) == list(range(1, 10)):
            checkedList.append(0)
        else: checkedList.append(1)
    return sum(checkedList)
def checkSudoku(puzzle):
    Check1 = checkRow(puzzle)
    Check2 = checkColumn(puzzle)
    Check3 = check3x3(puzzle)
    if Check1 + Check2 + Check3 == 0: return True
    else: return False

print(checkSudoku([[5,3,4,6,7,8,9,1,2], \
       [6,7,2,1,9,5,3,4,8], \
       [1,9,8,3,4,2,4,6,7], \
       [8,5,9,7,6,1,5,2,3], \
       [4,2,6,8,5,3,7,9,1], \
       [7,1,3,9,2,4,8,5,6], \
       [9,6,1,5,3,7,2,8,4], \
       [2,8,7,4,1,9,6,3,5], \
       [3,4,5,2,8,6,1,7,9]  ]))

print(checkSudoku([[5,3,4,6,7,8,9,1,2], \
       [6,7,2,1,9,5,3,4,8], \
       [1,9,8,3,4,2,5,6,7], \
       [8,5,9,7,6,1,4,2,3], \
       [4,2,6,8,5,3,7,9,1], \
       [7,1,3,9,2,4,8,5,6], \
       [9,6,1,5,3,7,2,8,4], \
       [2,8,7,4,1,9,6,3,5], \
       [3,4,5,2,8,6,1,7,9]  ]))
print("incineroar")
