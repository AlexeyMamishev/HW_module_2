def trap(n):
    z = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                z += str(i) + str(j)
    return f'{n} - {z}'

n = int(input("Введите число: "))

password = trap(n)
print(password)