#function that returns minimum and maximum values that can be calculated using a given array of 5 integers
def miniMaxSum(arr):    
    sortedArray = arr[:]
    sortedArray.sort()
    minimumArray = sortedArray[:]
    maximumArray = sortedArray[:]
    minimumArray.pop(4)
    maximumArray.pop(0)
    
    minArraySum = 0
    maxArraySum = 0
    
    for i in minimumArray:
        minArraySum += i
    
    for j in maximumArray:
        maxArraySum += j
    
    output = f'{minArraySum} {maxArraySum}'
    return output

print(miniMaxSum([1,2,3,4,5]))

#function to find median of an array
def findMedian(arr):
    arr.sort()
    arrayLength = len(arr)
    
    medianNum = int(arrayLength / 2)
    
    median = arr[medianNum]
    return median
    
    

print(findMedian([1,2,3,4,5]))
print(findMedian([1,2,3,4,5,6,7,8,9,10,11,12]))

#function to find which value in an array of all duplicates except one which one is the non-dupe.
def findLoneInteger(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
        else:
            continue


print(findLoneInteger([1,1,2,3,3,4,4,5,5,5]))

#function that given a square matrix returns the absolute difference of each diagonal (that is right to left diagonal - left to right diagonal)

def diagonalDifference(arr):
     leftPrimaryDiagonal = 0
     rightPrimaryDiagonal = 0
     for i in range(0,len(arr)):
         leftPrimaryDiagonal = leftPrimaryDiagonal + arr[i][i]
    
     for j in range(0,len(arr)):
         rightPrimaryDiagonal = rightPrimaryDiagonal + arr[j][len(arr)-1-j]
    
     return abs(leftPrimaryDiagonal - rightPrimaryDiagonal)

print(diagonalDifference([[11,2,4], [4,5,6], [10,8,-12]]))


#function that given a matrix will sort and add the 4 highest digits in the 0 and 1 indexes of each row col.
def sortAndSum(matrix):
    for item in matrix:
        item.sort(reverse=True)

    column_zero = [col[0] for col in matrix]
    column_one = [col_one[1] for col_one in matrix]
    sorted_column_zero = sorted(column_zero, reverse=True)
    sorted_column_one = sorted(column_one, reverse=True)
    
    iterator = 0
    total_sum = 0
    while iterator <= 1:
        total_sum += sorted_column_zero[iterator]
        total_sum += sorted_column_one[iterator]
        iterator = iterator + 1

    return total_sum

myMatrix = [[4,5,8,9], [1,3,6,7], [76,13,14,18], [25,7,6,2]]
print(sortAndSum(myMatrix))