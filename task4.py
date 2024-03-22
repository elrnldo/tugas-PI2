grades = []
total_sum = 0
print("Input the grades (Input -1 to end)")

while True:
  grade = int(input())
  if grade == -1:
    break
  grades.append(grade)
  total_sum += grade

if not grades:
  print("No grades entered.")
else:
  average = int(total_sum / len(grades))
  print(f"Average: {average}")
  for grade in grades:
    print(grade)