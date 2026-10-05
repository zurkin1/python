animal_list = []
animal_list.append('python')
animal_list.append('cat')
animal_list.append('lion')
animal_list.append('dog')
animal_list.append('mouse')
animal_list.append('tiger')
animal_list.append('fish')
animal_list.append('bug')

house_animal_list = []
for animal in animal_list:
    ans = input("Do you want to buy "+animal+" to be your pet?")
    if ans == "yes":
        house_animal_list.append(animal)
print("Your animal list:")
print(house_animal_list)
