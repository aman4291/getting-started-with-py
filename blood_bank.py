from unicodedata import name
print("Welcome to the blood bank inventory sir/madam \n")
# created data inventory-----

data_inventory=['Aman', '2000', 'Indore', 'A+', '23 march 2020', 'Annant', '1994', 'Banglore', 'B+', '7 july 2021', 'Pratik', '2001', 'Mangliya', 'A', 'Never', 'Sampada', '2002', 'Texas', 'B+', '14 november 2018', 'Krati', '2002', 'Mandsaur', 'O+', '3 november 2020']

# ---------To take inputs from users---------

def data_input():
    name = input("\nEnter your Name:\n")
    dob= input("Enter your Date of birth:\n")
    place= input("Where do you live?\n")
    blood_group= input("What is your Blood Group:\n")
    last_donated_date= input("Last time you donated blood(specify date):\n")

# To store inputs in list

    data_inventory.append(name)
    data_inventory.append(dob)
    data_inventory.append(place)
    data_inventory.append(blood_group)
    data_inventory.append(last_donated_date)