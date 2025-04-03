# Write a function called rotate_sequence that takes a sequence
# (string or list) and a number n as parameters. The function should return a
# new sequence with elements rotated to the right by n positions. If n is
# negative, rotate to the left instead.

# PSEUDOCODE
# Get two sub sequences as divided at index `n`
# join those two substrings according to whether `n` is negative or positive
# left = seq[-n:], right[:-2]

# if `n` is positive, the two substrings will be:
#   then join them `left` and `right`

# if `n` is negative:
#   join `right` to `left`

def rotate_sequence(seq, n):
    if n == 0:
        return seq
    
    if n > 0:
        return seq[-n:] + seq[:-n]
    else:
        return seq[abs(n):] + seq[:abs(n)]

def rotate_sequence(seq, n):
    if n == 0:
        return seq
    
    return seq[-(n):] + seq[:-(n)]
    
# Results:
print(rotate_sequence("Python", 2))    # Returns "onPyth"
print(rotate_sequence([1, 2, 3, 4, 5], -1))  # Returns [2, 3, 4, 5, 1]
print(rotate_sequence([1, 2, 3, 4, 5], -3))  # Returns [4, 5, 1, 2, 3]
print(rotate_sequence("Python", 0))  # Returns "Python"