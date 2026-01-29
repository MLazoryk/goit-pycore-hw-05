def cauching_fibonacci():
    """
    This function creates and returns a Fibonacci calculator with memory.
    """


    cache = {}

    def fibonacci(n):

        """
        Calculating the n-th Fibonacci number.
        Uses caching (memory to avoid recalculating numbers)

        Parameters: n (int): Which number to calculate (e.g. 5th, 10th, etc.)

        Returns:
        int: The n-th Fibonacci number
        """

        if n <= 0:
            return 0
        
        if n == 1: 
            return 1
        
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

# Example usage: 
if __name__ == "__main__":
    fib = cauching_fibonacci()
    print(fib(10))
    print(fib(50))
    print(fib(100))
    