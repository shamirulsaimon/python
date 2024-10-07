def life_in_weeks(age):
 age_left = 90 - age
 weeks_left = age_left*52
 print(f"You have {weeks_left} weeks left")

current_age = int(input("Enter Your Current Age This Year: "))
life_in_weeks(current_age)
