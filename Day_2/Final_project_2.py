print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? : "))
tip_per = float(input("What percentage tip would you like to give? : "))
people_split = int(input("How many people to split the bill? : "))

each_bill = (total_bill / people_split) + ((total_bill * (tip_per/100)) / 5)
final_bill = "{:.2f}".format(each_bill)
print(f"Each person should pay $ {final_bill}")
