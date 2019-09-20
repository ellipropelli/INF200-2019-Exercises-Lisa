def squares_by_loop(n):
    square = []
    for k in range(n):
        if k % 3 == 1:
            square.append(k**2)
    return square
print (squares_by_loop(10))


