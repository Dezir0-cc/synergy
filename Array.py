A = list(map(int, input().split()))

max_index = A.index(max(A))
min_index = A.index(min(A))

start = min(max_index, min_index)
end = max(max_index, min_index)

sum_neg = 0

for i in range(start + 1, end):
    if A[i] < 0:
        sum_neg += A[i]

print(sum_neg)