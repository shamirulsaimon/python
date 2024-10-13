def calculate_love_score(name1, name2):
  combined_names = name1 + name2
  lower_case_names = combined_names.lower()
  t = lower_case_names.count("t")
  r = lower_case_names.count("r")
  u = lower_case_names.count("u")
  e = lower_case_names.count("e")
  l = lower_case_names.count("l")
  o = lower_case_names.count("o")
  v = lower_case_names.count("v")
  e = lower_case_names.count("e")
  love_score = str(t + r + u + e) + str(l + o + v + e)
  print(love_score)
calculate_love_score("Kanye West", "Kim Kardashian")