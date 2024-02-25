n_list = list(map(int, input().split()))

n_result = 0

if n_list[0] > n_list[1]:
    n_result = n_list[0] * n_list[1]
else :
    n_result = n_list[1] / n_list[0]

print(n_result)