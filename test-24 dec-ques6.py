import heapq
from heapq import heappop
 
def find_kth_smallest(input, k):
    if not input or len(input) < k:
        exit(-1)
    heapq.heapify(input)
    while k > 1:
        heappop(input)
        k = k - 1
    return input[0]

input = [7, 10, 4, 3, 20, 15]
k = 3
print('k\'th smallest element in the list is', find_kth_smallest(input, k))