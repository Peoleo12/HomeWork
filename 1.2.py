time = int(input("Enter your time in sec: "))
hours = time // 3600
residue = time % 3600
minutes = residue // 60
seconds = residue % 60
print(f"Now is {hours}:{minutes}:{seconds} ")
