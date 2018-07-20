Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
    O(n). It looks pretty linear, but ultimately I am still a bit fuzzy about
    Big O notation
2. What is the space complexity of your `depth_first_for_each` function?
    O(n), visiting each node only once.

3. What is the runtime complexity of your `breadth_first_for_each` method?
    unsure
    O(n)
4. What is the space complexity of your `breadth_first_for_each` method?
    unsure
    O(n)
5. What is the runtime complexity of your `heapsort` function?
    O(n log n) at worst the heap has a height of log n, and because it does this n times we get O(n log n)... I think
    just kidding my answer has a time complexity of O(n^2)
    solution lecture code is O(n log n)
    so if done correctly it is O(n log n), but my code was writting poorly.

6. What is the space complexity of the `heapsort` function? Recall that your implementation should return a new array with the sorted data. What would be the space complexity if your function instead altered the input array?
    if it altered the input array it would be O(1), but with it returning the array? I am unsure how much that adds to the space complexity. But because the space allocated needs to grow based on the size of the array it would be O(n)?
    Maybe?