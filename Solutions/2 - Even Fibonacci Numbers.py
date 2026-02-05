def fib(n):
    limit = 4000000
    total_fib = 0
    a, b = 1 ,2

    while a <= limit:
        # if number is even, add it to the total
        if a % 2 == 0:
            total_fib += a

        # update values
        a, b = b, a + b
    
    return total_fib

print (f"The sum of even-valued Fibonacci terms below 4 million is: {fib(4000000)}")