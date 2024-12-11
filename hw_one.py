def caching_fibonacci():
    """
    Returns a Fibonacci function with caching.

    This function creates and returns a nested `fibonacci` function that calculates 
    Fibonacci numbers using recursion with memoization to optimize performance. 
    The computed values are stored in a cache to avoid redundant calculations.

    Returns:
        function: A function that computes the nth Fibonacci number efficiently.
    """
    cache = {}

    def fibonacci(n):
        """
        Calculates the nth Fibonacci number using recursion with caching.

        Args:
            n (int): The position in the Fibonacci sequence (0-based index).

        Returns:
            int: The nth Fibonacci number.
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n -1) + fibonacci(n - 2)
            return cache[n]
    return fibonacci

fib = caching_fibonacci()
print(fib(10))
print(fib(15))
        
