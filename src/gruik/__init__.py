from concurrent.futures import ProcessPoolExecutor


def callback(x):
    return 1


def f():
    with ProcessPoolExecutor() as pool:
        return list(pool.map(callback, range(1000)))
