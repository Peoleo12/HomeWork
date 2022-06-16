from sys import argv

file_name, production_in_hours, rate_pre_hour, premium = argv

calculation = (int(production_in_hours) * int(rate_pre_hour)) + int(premium)
print(f"Your pay is equal {calculation}")
