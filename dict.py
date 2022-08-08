dict = {
        "name": "annant",
        "dob": "1",
        "place": "indore",
        "blood_group": "9806",
        "last_donated_date": "24",
    }
new_dict={
    "name": "aman",
    "dob": "2",
    "place": "satna",
    "blood_group": "A",
    "last_donated_date": "3",
}
    # {
    #     "name": "robert",
    #     "dob": "3",
    #     "place": "deora",
    #     "blood_group": "O",
    #     "last_donated_date": "30"
    # }


dict1=dict.copy()
print(dict1)

dict2=dict.keys()
print(dict2)

dict3=dict.get("name")
print(dict3)

dict4=dict.values()
print(dict4)

dict5=dict.popitem()
print(dict5)

# dict6=dict.clear()
# print(dict6)

dict7=dict.items()
print(dict7)

dict8=dict.update(new_dict)
print(dict)

