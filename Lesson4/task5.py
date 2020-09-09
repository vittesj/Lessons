print(__import__('functools').reduce(lambda j, k: j * k, [i for i in range(100, 1001) if i % 2 == 0]))
