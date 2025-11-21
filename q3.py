n = int(input())
arr = list(map(int, input().split()))
l, r = map(int, input().split())

total = 0
for i in range(l - 1, r):
    total += arr[i]

print(total)