# Q7:Managing
N, K = map(int, input().split())
seq = [0] * N             # danh sách các biến được nhập vào
d = [0] * N            # danh sách lưu trữ giá trị lớn nhất đạt được tại mỗi vị trí
prefixSeq = [0] * N #danh sách lưu tổng tiền tố

for i in range(N):
    seq[i] = int(input())

for i in range(N):
    if i == 0:
        prefixSeq[i] = seq[i]
    else:
        prefixSeq[i] = prefixSeq[i - 1] + seq[i]

for i in range(N):
    if i == 0:
        d[i] = seq[i]
    elif i < K:
        d[i] = d[i - 1] + seq[i]
    else:
        for j in range(i - K, i):
            d[i] = max(d[i], d[j - 1] + prefixSeq[i] - prefixSeq[j])

print(max(d))