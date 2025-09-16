
skills = {
    "Работа со списками": 90,
    "Работа со словарями ": 60,
    "Система счисления": 50,
    "Работа с массивами ": 30,
    "C++": 40
}
def analyze_skills():

    min_skill_name = min(skills, key=skills.get)
    max_skill_name = max(skills, key=skills.get)

    min_skill_value = skills[min_skill_name]
    max_skill_value = skills[max_skill_name]
    return min_skill_name, min_skill_value, max_skill_name, max_skill_value
min_skill_name, min_skill_value, max_skill_name, max_skill_value = analyze_skills()
print(f"Наименее популярный навык: {min_skill_name} (в %): {min_skill_value}")
print(f"Наиболее популярный навык: {max_skill_name} (в %): {max_skill_value}")



#skills = [25, 30, 15, 40, 50, 60]
#def analyze_skills(skills):
 ##   max_skill = max(skills)
##   min_skill = min(skills)

#  print(f"Доля питонистов, у которых есть наименее популярный навык (в %): {min_skill}")
 #   print(f"Доля питонистов, у которых есть наиболее популярный навык (в %): {max_skill}")
#analyze_skills(skills)
