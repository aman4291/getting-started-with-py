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

# --------To show-all user data---------

def show_all_data():
    for index in range(0, len(data_inventory), 5):
        print("Name: ", data_inventory[index])
        print("dob: ", data_inventory[index+1])
        print("place: ", data_inventory[index+2])
        print("blood_group: ", data_inventory[index+3])
        print("last_donated_date: ", data_inventory[index+4])
        print("\n")

# -------to search user data-----------

def search_data():
    name=input("\nEnter the name of user : \n")
    for index in range(0, len(data_inventory), 5):
        if (name == data_inventory[index]):
           print("\nThis user data is present in this list :\n",
           data_inventory[index], data_inventory[index+1], data_inventory[index+2], data_inventory[index+3], data_inventory[index+4]) 
           return index

        elif len(data_inventory)-5 == index:
            print("Error: Data not found")
            return None

# ------------To update user data---------

def update_user_data():
    index= search_data()
    if index == None:
        return 

    print("Enter the values to update User: \n")

    data_inventory[index]= input("Enter name: \n")
    dob=input("Enter Date of Birth: \n")
    data_inventory[index+1]= dob
    place=input("Enter the name of city: \n")
    data_inventory[index+2]= place
    blood_group=input("Enter Blood Group: \n")
    data_inventory[index+3]= blood_group
    last_date=input("Enter the last date when user has donated blood: \n")
    data_inventory[index+3]= last_date

# ------------To delete user data---------
           
def delete_user():
    print("\nSearch the user's name, whom data you want to delete")
    index= search_data() 
    if index is None:
        return False
    print("\n",data_inventory)
    last_donation_date = data_inventory.pop(index+4)
    blood_goup = data_inventory.pop(index+3)
    place = data_inventory.pop(index+2)
    dob =data_inventory.pop(index+1)
    name = data_inventory.pop(index)

    print(f'\nThe user {name} has been removed from the inventory')
    return True

# Below code will take action input from the users

def main():
    choice = 1
    while(choice):
        print("A: Add User  \t B: Showall Users  \t C: Search User  \t D: Delete User  \t E: Update User  \t X: exit")
        choice = (input("\nEnter your choice : "))
        if(choice == 'X'):
            print("Thanks for visiting our Application")
        elif(choice == 'A'):
            print("\nAdd new User")
            data_input()   
        elif(choice == 'B'):
            print("\nDisplaying all users data\n")
            show_all_data()    
        elif(choice == 'C'):
            search_data()   
        elif(choice == 'D'):
            delete_user()        
        elif(choice == 'E'):
            update_user_data()
main()