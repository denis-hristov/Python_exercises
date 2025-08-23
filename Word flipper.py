def reverse(text):
  word = ""
  for n in range(len(str(text))-1, -1, -1):
    word += str(text)[n]
  return word