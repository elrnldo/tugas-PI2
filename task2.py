total_sum = 0.0
print("Input your number (Input -1 to end)")
while True:
  number = float(input())
  if number == -1:
    break
  total_sum += number

print(f"The sum of all numbers is: {total_sum:.2f}")