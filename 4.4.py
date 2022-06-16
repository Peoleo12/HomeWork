from itertools import permutations
from itertools import repeat
from itertools import combinations

my_list = [2, 3, 4, 5, 4, 3, 2]
new = [el for el in my_list if my_list.count(el) == 1]
print(new)
