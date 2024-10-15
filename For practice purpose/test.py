student_scores = {"sr":"60",
                  "rs":"65",
                  "TS":"70",
                  "RS":"75",
                  "ar":"80",
                  "YS":"90"}

def grade_system(score):
  if score>=90:
    return "A+"
  elif score <90 and score >=80:
    return "A"
  elif score <80 and score >=70:
    return "A-"
  elif score < 70 and score >=60:
    return "B+"
  elif score < 60 and score >=50:
    return "B"
  elif score <50 and score >=40:
    return "C+"
  else:
    return "Fail"

Grade = {}

for student , score in student_scores.items():
   Grade[student] = grade_system(int(score))


print(Grade)