def ft_fibonacci(index):
    if index < 0:
        return -1
    if index == 0:
        return 0
    if index == 1:
        return 1
    return ft_fibonacci(index - 1) + ft_fibonacci(index - 2)
#def factorial(n):
    #if n == 0:
        #return 1
    #else:
        #return n * factorial(n - 1)