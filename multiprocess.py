import time
from multiprocessing import Pool


def square(x):
    print(f"start process:{x}")
    square = x * x
    print(f"square {x}:{square}")
    time.sleep(1)
    print(f"end process:{x}")


def cube(y):
    cube = y*y*y
    print(f"cube{y}:{cube}")
    time.sleep(1)
    print(f"end process:{y}")


if __name__ == "__main__":
    starttime = time.time()
    pool = Pool()
    pool.map(square, range(0, 5))
    pool.map(cube, range(0, 5))
    pool.close()
    endtime = time.time()
    print(f"Time taken {endtime-starttime} seconds")
