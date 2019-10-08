import numpy as np

SEED = 9999
MAX_POWER = 22

def main():
    np.random.seed(SEED)
    for i in range(2, MAX_POWER + 1):
        n = 2**i
        np.savetxt('{}.txt'.format(n), np.random.uniform(size=n))


if __name__ == '__main__':
    main()

