print("Magic Square Checker")
n = int(input("Enter size of square: "))
total_sum = 0
row_sum = 0
i = 0
while i < n:
j = 0
row_sum = 0
while j < n:
value = int(input("Enter number: "))
row_sum = row_sum + value
j = j + 1
if i == 0:
total_sum = row_sum
else:
if row_sum != total_sum:
print("Not Magic Square")
i = i + 1
if row_sum == total_sum:
print("Magic Square")
else:
print("Not Magic")
if total_sum % 2 = 0:
print("Even magic constant")
else:
print("Odd magic constant")