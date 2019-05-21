"""
Maximize the distribution of chocolate among k no of student equally
by selecting a sequence of chocolate boxes from given array.
let arr = [2,7,6,1,4,5] and k = 3
then output is 6 chocolate to each students
[7,6,1,4] = 18

"""
# Dynamic Programming
def chocolate_distrubution(arr, k):
    hash_table = {}
    max_sum = 0
    n = len(arr)

    # calculate cummulative sum
    for i in range(1, n):
        arr[i] += arr[i-1]

    print arr
    #import pdb; pdb.set_trace()

    for i in range(0, n):
        remainder = arr[i] % k
        if remainder == 0 and max_sum < arr[i]:
            max_sum = arr[i]
        elif remainder != 0 and remainder not in hash_table.keys():
            hash_table[remainder] = i
        else: 
            #remainder is in hash_table
            if max_sum < (arr[i] - arr[hash_table[remainder]]):
                max_sum = arr[i] - arr[hash_table[remainder]]
    return max_sum/k

if __name__ == '__main__':

    k = 3
    #arr = [2,7,6,1,4,5]
    arr = [2,7,6,1,4,5,4,8]

    print chocolate_distrubution(arr, k)
