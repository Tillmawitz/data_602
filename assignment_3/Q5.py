numerator = list(range(1,31))
denominator = sorted(list(range(1,31)), reverse=True)
sum = 0

for ind, num in enumerate(numerator):
    sum += num / denominator[ind]

print(sum)