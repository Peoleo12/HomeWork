my_list = [11, 22, 5, 3, 1, 12, 22, 9, 99]
new = [el for el in my_list if el > my_list[my_list.index(el) - 1]]
print(new)



i = 0
new= []
for el in my_list:
    if el > my_list[i-1]:
        new.append(el)
    i+=1
print(new)