def purify(lists):
  new_list = []
  for n in lists:
    if n % 2 == 0:
      new_list.append(n)
  return new_list