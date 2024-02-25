n_list = list(map(int, input().split(" ")))
sum_n = sum(n_list)
avg_n = sum_n / len(n_list)

print(f"{sum_n} {avg_n:.1f}")