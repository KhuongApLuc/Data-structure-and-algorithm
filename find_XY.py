#Q2: XY
def get_char(n, k):
    if n == 1:
        return 'X'
    mid = 2**(n-2)
    if k <= mid:
        return get_char(n-1, k)
    else:
        return 'Y' if get_char(n-1, k-mid) == 'X' else 'X'

def main():
    numOfRequire = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(numOfRequire)]

    results = []
    for n_i, k_j in queries:
        if 1 <= n_i <= 30 and 1 <= k_j <= 2**(n_i - 1):
            results.append(get_char(n_i, k_j))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()