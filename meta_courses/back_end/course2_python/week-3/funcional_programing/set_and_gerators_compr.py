# SET
set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)

# GER
data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")