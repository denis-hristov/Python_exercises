def remove_duplicates(list):
  new_list = []
  for n in list:
    if len(new_list) == 0:
      new_list.append(n)
    else:
      found = False
      for i in new_list:
        if i == n:
          found = True
          break
      if not found:
        new_list.append(n)
  return new_list