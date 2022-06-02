firm = {'Andy': 20000, 'Alex': 21000, 'Leonid': 19000, 'Dmitriy': 23000}
try:
    file_obj = open("test_3.txt", 'w')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Error")
finally:
    file_obj.close()
sum = 0
count = 0
persons = []
with open("test_3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 200:
            persons.append(tokens[0])
        sum += int(tokens[1])
        count += 1
result = sum / count
print(f"persons: {persons}")
print(f"average: {result}")