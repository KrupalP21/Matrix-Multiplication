# Create First Matrix
firstMatrixSizeInput = input()
firstMatrixSize = firstMatrixSizeInput.split()

firstMatrix = []
for i in range(int(firstMatrixSize[0])):
    firstMatrix.append([])
    
for i in range(int(firstMatrixSize[0])):
    temp = input()
    currentRow = temp.split()
    for j in range(len(currentRow)):
        firstMatrix[i].append(float(currentRow[j]))

# Create Second Matrix        
secondMatrixSizeInput = input()
secondMatrixSize = secondMatrixSizeInput.split()

secondMatrix = []
for i in range(int(secondMatrixSize[0])):
    secondMatrix.append([])
    
for i in range(int(secondMatrixSize[0])):
    temp2 = input()
    currentRow2 = temp2.split()
    for j in range(len(currentRow2)):
        secondMatrix[i].append(float(currentRow2[j]))
if (len(firstMatrix[0]) != len(secondMatrix)):
    print("invalid input")
else:          
# Create Result Matrix
    result = []
    for i in range(int(firstMatrixSize[1])):
        result.append([])

# Perform Multiplication with Matrices
    for i in range(0, len(firstMatrix)):
        for j in range(0, len(secondMatrix[0])):
            result[i].append(0.0)
            for k in range(0, len(secondMatrix)):
                result[i][j] += firstMatrix[i][k] * secondMatrix[k][j]

    for i in range(len(result)):
        for j in range(len(result[0])):
            print(*result[i])
    