age = input("What is your current age?: ")

age_int = int(age)
years = 70 - age_int
months = (years * 12)
weeks = (years * 52)
days = (years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left :(")
