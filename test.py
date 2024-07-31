def binary_search_helper(x, A, i, j):
    '''
    Searches A for an element x using binary search. Returns the index of x if
    x is in A, or -1 if x is not in A.

    i is a lower bound on the index of x in A, and j is an upper bound on the
    index of x in A.
    '''
    if i > j:
        return -1

    mid = (i + j) // 2

    if A[mid] == x:
        return mid
    elif A[mid] > x:
        return binary_search_helper(x, A, i, mid-1)
    else:
        return binary_search_helper(x, A, mid+1, j)

def find_all_indices(x, A):
    '''
    Finds all indices of x in the sorted array A.
    '''
    index = binary_search_helper(x, A, 0, len(A)-1)
    if index == -1:
        return []

    # Find the first occurrence
    first = index
    while first > 0 and A[first-1] == x:
        first -= 1

    # Find the last occurrence
    last = index
    while last < len(A)-1 and A[last+1] == x:
        last += 1

    # Return all indices from first to last
    return list(range(first, last + 1))

# Example usage
A = [1, 3, 5, 7, 9, 11, 11, 11, 15, 17, 19]
x = 11

# Find all indices of x
result = find_all_indices(x, A)

# Output the result
print(f"Element {x} found at indices: {result}")
