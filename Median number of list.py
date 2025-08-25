def median(numbers):
  num = 0
  numbers.sort()
  lenght = len(numbers) / 2
  if len(numbers) % 2 == 0:
    num = float(numbers[lenght] + numbers[lenght - 1]) / 2
  else:
    num = numbers[int(lenght)]
  return num