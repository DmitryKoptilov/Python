sum = 0
count = 0
max_num = None
min_num = None
even_count = 0
odd_count = 0

while True:
    num = int(input("number: "))
    if num == 0:
        break
    sum += num
    count += 1
    if max_num is None or num > max_num:
        max_num = num
    if min_num is None or num < min_num:
        min_num = num
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if count > 0:
    avg = sum / count
else:
    avg = 0

print("Number of entered numbers:", count)
print("Sum of entered numbers:", sum)
print("Arithmetic average:", avg)
print("Maximum value:", max_num)
print("Minimum value:", min_num)
print("Number of even numbers:", even_count)
print("Number of odd numbers: ", odd_count)