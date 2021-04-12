def fact(n):
    if n:
        n = n*fact(n-1)
        return n
    else:
        return 1

print(fact(int(1.5)))