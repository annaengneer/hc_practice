import random
g_list = ['A', 'B', 'C', 'D', 'E', 'F']
number =[3,4]
shuffle = random.sample(g_list, len(g_list))
choice_number = random.choice(number)
for i in range(0,len(shuffle), choice_number):
    print(sorted(shuffle[i:i+choice_number]))