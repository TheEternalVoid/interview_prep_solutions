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


#Defines a function that given a list of integers will print the ratio of positive,
#negative, and zeroes.
def plusMinus(arr):
    # set tracker values
    positive_num = 0
    negative_num = 0
    zeroes = 0
    array_length = len(arr)
    
    #find how many positive nums, negative, and zeros
    for num in arr:
        if num > 0:
            positive_num = positive_num + 1
        elif num < 0:
            negative_num = negative_num + 1
        elif num == 0:
            zeroes = zeroes + 1
            
    #divide the amount of each num by the total num of items in the list      
    positive_num_ratio = positive_num / array_length
    negative_num_ratio = negative_num / array_length
    zeroes_num_ratio = zeroes / array_length

    #print out the decimals for each amount
    print(format(positive_num_ratio, '.6f'))
    print(format(negative_num_ratio, '.6f'))
    print(format(zeroes_num_ratio, '.6f'))

plusMinus([1,2,3,-2,-2,4,0,0])

#Given a list find sum and mode and return as a list of both results.
def meanAndMode(inputArr):
    #for eachNum in inputArr sum = sum + inputArr[eachNum]

    #inputArrMode = count through the arr and add up which has the most occurances. Add that to final answer array
    inputArrSum = 0
    finalAnswer = []

    for i in inputArr:
        inputArrSum = inputArrSum + i

    numCounts = {}
    # iterate through the list 
    for item in inputArr:
        if item in numCounts:
            numCounts[item] += 1
        else:
            numCounts[item] = 1

    max_key = max(numCounts, key=numCounts.get)
    
    #append each result to final return
    finalAnswer.append(inputArrSum)
    finalAnswer.append(max_key)
    return finalAnswer

print(meanAndMode([1,2,3,4,6,9,4,5,7,6]))

#given a string in 12hour clock format (hh:mm:ssAM/PM) Return a 24 hour clock conversion
def timeConversion(s):

    #check if am or pm
    if s[8] == "A":
        first_two_digits = int(s[:2])

        #if its 12:00 AM we need to make the time 00
        if first_two_digits == 12:
            first_two_digits_converted = 00
            #make sure theres 2 zeroes
            first_two_digits_converted = f"{first_two_digits_converted:02d}"
            first_two_digits_converted = str(first_two_digits_converted)

        else:
            first_two_digits_converted = first_two_digits + 00
            first_two_digits_converted = f"{first_two_digits_converted:02d}"
            first_two_digits_converted = str(first_two_digits_converted)

        #create a list of characters from the string
        s_updated = list(s)
        
        #insert the new digits into the correct indexes
        s_updated[0] = first_two_digits_converted[0]
        new_s = "".join(s_updated)
        s_updated[1] = first_two_digits_converted[1]
        new_s = "".join(s_updated)
        
        #find length of string to cut off am or pm
        string_size = len(new_s)
        cut_am_pm = new_s[:string_size -2]
        
        return cut_am_pm
    
    elif s[8] == "P":
        first_two_digits = int(s[:2])
        #if it's 12 we don't need to add any additional digits
        if first_two_digits == 12:
            first_two_digits_converted = 12
            first_two_digits_converted = str(first_two_digits_converted)
        #if its not 12 we need to add the first two digits + 12
        else:
            first_two_digits_converted = first_two_digits + 12
            first_two_digits_converted = str(first_two_digits_converted)

        #create a list of characters from the string
        s_updated = list(s)
        
        #insert the new digits into the correct indexes
        s_updated[0] = first_two_digits_converted[0]
        new_s = "".join(s_updated)
        s_updated[1] = first_two_digits_converted[1]
        new_s = "".join(s_updated)
        
        #find length of string to cut off am or pm
        string_size = len(new_s)
        cut_am_pm = new_s[:string_size -2]
        
        return cut_am_pm


print(timeConversion("10:05:45PM"))