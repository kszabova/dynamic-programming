n = int(input())

ugly_numbers = []
ugly_numbers.append(1) # 1 is an ugly number
i2 = i3 = i5 = 0
multiple_of_2 = ugly_numbers[i2] * 2
multiple_of_3 = ugly_numbers[i3] * 3
multiple_of_5 = ugly_numbers[i5] * 5

for i in range(1, n):
    next_ugly_number = min(multiple_of_2, multiple_of_3, multiple_of_5)
    ugly_numbers.append(next_ugly_number)

    if next_ugly_number == multiple_of_2:
        i2 += 1
        multiple_of_2 = ugly_numbers[i2] * 2
    if next_ugly_number == multiple_of_3:
        i3 += 1
        multiple_of_3 = ugly_numbers[i3] * 3
    if next_ugly_number == multiple_of_5:
        i5 += 1
        multiple_of_5 = ugly_numbers[i5] * 5

print(ugly_numbers[n - 1])
