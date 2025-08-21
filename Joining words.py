n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result = ""
  for n in words:
    result += n
  return result


print join_strings(n)