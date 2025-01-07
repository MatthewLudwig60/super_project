def add_arrays(x, y):
    z = []
    for x_, y_ in zip(x, y):
        z.append(x_ + y_)
    return z
