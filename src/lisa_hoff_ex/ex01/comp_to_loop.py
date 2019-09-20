def squares_by_loop(n):
    square = []
    for k in range(1, 14):
        if k % 3 == 1:
            square.append(k**2)
    return square


