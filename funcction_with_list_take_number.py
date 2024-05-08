def sum_of_list(s):
  sum = 0
  average=0
  for i in s:
    sum += i 
    average=sum/i 
  return sum
  git

z = [12, 45, 53, 4, 67]
result = sum_of_list(z)
print(f"{result}")


