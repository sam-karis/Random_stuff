# 0, 1, 1, 2, 3, 5


# Naive alogarithm
def naive_fibanacci(n):
    if n <= 1:
        return n
    else:
        return naive_fibanacci(n-1) + naive_fibanacci(n - 2)

num = int(input('Input the numbers :  '))
print(naive_fibanacci(num))

# A little efficient
def  Fibonacci(n):
    res = [0, 1]
    for i in range(n):
        next_num = res[i] + res[i+1]
        res.append(next_num)
    return ','.join(str(x) for x in res)


print(Fibonacci(num))