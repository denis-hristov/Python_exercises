word = raw_input("Enter a word: ")
if len(word) < 2:
  print "Error!"

pig_latin = word[1:] + word[0].lower() + "ay"

print pig_latin