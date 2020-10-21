# What's the variance of a uniform distribution defined on [0,6]?

# mean = 1/2(a+b)
# variance = 1/12(b - a)^2
# skewness = 0
# kurtosis = -6/5

def cal_variance(a, b):
    diff = b - a
    res = (diff^2)/12
    return res

print('Variance is :', cal_variance(0, 6))