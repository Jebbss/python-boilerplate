import multiprocessing as mp
from tqdm import tqdm


def square(x, id):
    print(f'Process {id} is squaring {x}')
    return x * x


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ids = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    with mp.Pool() as pool:
        jobs = [pool.apply_async(func=square, args=(*arg,)) for arg in zip(numbers, ids)]

        for job in tqdm(jobs, total=len(numbers), desc='Squaring numbers'):
            result = job.get()
            print(result)


if __name__ == '__main__':
    main()
