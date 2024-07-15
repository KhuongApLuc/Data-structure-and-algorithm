#Q6:RectangleMatrix
def maximalRectangle(matrix):
    if not matrix:
        return 0

    n = len(matrix)
    m = len(matrix[0])
    h = [0] * (m + 1)
    ans = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '1':
                h[j] += 1
            else:
                h[j] = 0

        stack = [] #lưu vị trí
        for j in range(m + 1):
            while stack and h[j] <= h[stack[-1]]:
                height = h[stack.pop()]
                width = j if not stack else j - stack[-1] - 1 #độ rộng là khối ở giữa
                ans = max(ans, height * width)
            stack.append(j)

    return ans

N, M = map(int, input().split())

matrix = []

for i in range(N):
    row = list(map(str, input().split()))
    matrix.append(row)

maximalRectangle_ = maximalRectangle(matrix)
print(maximalRectangle_)