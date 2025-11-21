n = int(input())
arr = list(map(int, input().split()))

total = 0
for i in range(n):
    total += arr[i] * (i + 1) * (n - i)

print(total)