number = int(input("Enter month number: "))
if number <= 12 and number >= 1:
    month_dict = {1: 'January',
                  2: 'February',
                  3: 'March',
                  4: 'April',
                  5: 'May',
                  6: 'June',
                  7: 'Jule',
                  8: 'August',
                  9: 'September',
                  10: 'October',
                  11: 'November',
                  12: 'December'}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == number - 1:
            print(f"Month from list is {month_list[i]}")
            break
    print(f"Month from dict is {month_dict[number]}")
else:
    print("Mistake")
