def anti_vowel(text):
  words = ""
  for i in text:
      if i.lower() not in "aeiou":
        words += i
  return words