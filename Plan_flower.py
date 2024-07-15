#Q5: Flow
MOD = 10**9 + 7

def matrix_mult(A, B):
    return [[sum(x * y for x, y in zip(A_row, B_col)) % MOD for B_col in zip(*B)] for A_row in A]

def matrix_pow(A, n):
    result = [[1 if i == j else 0 for j in range(len(A))] for i in range(len(A))]
    while n:
        if n % 2:
            result = matrix_mult(result, A)
        A = matrix_mult(A, A)
        n //= 2
    return result

def count_flower_arrangements(N):
    if N == 1:
        return 5
    
    initial_state = [1, 1, 1, 1, 1]
    
    A = [
        [0, 1, 0, 0, 0],  # H_n+1 = L_n
        [1, 0, 1, 0, 0],  # L_n+1 = H_n + M_n
        [1, 1, 0, 1, 1],  # M_n+1 = H_n + L_n + N_n + T_n
        [0, 0, 1, 0, 1],  # N_n+1 = M_n + T_n
        [1, 0, 0, 0, 0],  # T_n+1 = H_n
    ]
    A_N_minus_1 = matrix_pow(A, N - 1)
    final_state = [sum(A_N_minus_1[i][j] * initial_state[j] for j in range(5)) % MOD for i in range(5)]
    return sum(final_state) % MOD

N = int(input())
print(count_flower_arrangements(N))
