def subarray(seq):
    i = Sum = maxSum = 0
    start, end = 0, -1
    for j in range(len(seq)):
        Sum += seq[j]
        if Sum > maxSum:
            maxSum = Sum
            start = i
            end   = j
        elif Sum < 0:
            Sum = 0
            i = j + 1
    return (maxSum, start, end)
lst = [4, -1, 5, 6, -13, 2]
maxSum, start, end = subarray(lst)
print ("sum is:",maxSum)
print("subarray:",lst[start:end+1])