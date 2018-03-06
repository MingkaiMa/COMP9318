import math


def f(x):
    return x * math.log(x) - 16.0

def fprime(x):
    return 1.0 + math.log(x)


def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000): # do not change the heading of the function
    for i in range(MAX_ITER):
        ff = f(x_0)
        fp = fprime(x_0)

        x_new = x_0 - ff / fp

        if(abs(x_new - x_0) < EPSILON):
            return x_new

        x_0 = x_new


    return x_new


if __name__ == '__main__':
    x = find_root(f, fprime)
    print(x)
    print(f(x))

        

