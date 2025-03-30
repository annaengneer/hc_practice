import random
g = ['A', 'B', 'C', 'D', 'E', 'F']
s = random.sample(g, len(g))
new_g1 = s[:2]
new_g2 = s[2:]
print(sorted(new_g1))
print(sorted(new_g2))