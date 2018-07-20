Add your answers to the Algorithms exercises here.
all answers are from solution lecture
a) O(n) while loop is O(n^3) inside while loop is O(n^2), which gives us O(n)
b) O(log n)
c) O(1) these are just constant loops O(sqrt(n))
d) O(n log n) for loop is O(log n) inner for loop is O(n)
e) O(n^3)
f) O(n)  
g) O(n) worst case has to recurse to beginng of array so O(n)

ex II
a) 
    minVal = a[0]
    maxDiff = 0

    for i in l..n
    minVal = min(minVal, a[i])
    maxDiff = max(maxDiff, a[i] - minVal)
    return maxDiff
    O(n)

b) binary search, start at the middle (n/2) drop an egg, if it breaks half it again
    if you drop one from the middle and it doesnt break, increase by 3/4ths and drop an egg.
    O(log n) for binary
    if starting from bottom and moving up one floor at a time
    O(n)
    """ Troy Bradley's answer
    I'd start on the 3rd floor. If the egg breaks, go to the second floor and try again. If it doesn't break, go to the 6th floor. Basically, if the egg doesn't break, go up 3 floors. If it does break, go down 1.
    """

ex III

a) O(n^2)
b) O(n log n)

