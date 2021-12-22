# Pascal's Triangle to compute the coefficients
# of binomials and return the expanded formula

# int n as param representing exponent for binomial expansion
# return level n, (x+y)^n, as well as 2^n and 11^n
def pascals_secrets(n):
    list = []
    for n in range(n+1):
        list.append([])
        list[n].append(1)
        for m in range(1, n):
            list[n].append(list[n - 1][m - 1] + list[n - 1][m])
        if(n != 0):
            list[n].append(1)
    # Return each row including the one inputted
    # print(list)
    # Revise to use list comprehension to return the coef
    for m in range(0, n + 1):
        print(f'{list[n][m]}')
    print()


# Driver program
n = 4
pascals_secrets(n)
