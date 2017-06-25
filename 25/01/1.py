import timeit

def loop_range():
    return range(100, 1, 1)
def loop_for():
    a = []
    for i in range(100):
        a.append(i+1)
    return a
def loop_listin():
    return [i+1 for i in range(100)]

timeit.__dict__.update(loop_for=loop_for, loop_listin=loop_listin, loop_range=loop_range)
print(timeit.Timer('loop_range()').timeit(1))
print(timeit.Timer('loop_for()').timeit(1))
print(timeit.Timer('loop_listin()').timeit(1))

