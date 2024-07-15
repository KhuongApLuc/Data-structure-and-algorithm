#Sample: A plus B
N = int(input())
n = 1
results = []

while n<=N: 
    a, b = map(int, input().split())
    result = a+b
    results.append(result)
    n = n+1

for i in results:
    print(i)

N = int(input())
