menu = ['expresso','cappuccino','latte','mocha','cortado','americano']

def find_coffee(list_menu):
    if list_menu[0]=='C':
        return list_menu
    
map_tittle = [*map(str.capitalize,menu)]
print(map_tittle)

filter_coffee = [*filter(find_coffee,map_tittle)]
print(filter_coffee)

a = [[96],[69]]
a_mad = ''.join(list(map(str,a)))
print(type(a_mad), a_mad)