def summary():
    try:
        with open('test_5.txt', 'w+') as file_obj:
            line = input('Enter numbers separated by spaces \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Error in file')
    except ValueError:
        print('Input error')


summary()
