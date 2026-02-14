# dict={
#     "Name":"Sandeep MUhal",
#     "Age": 45,
#     'Cgpa':6.48,
#     "Marks":[15,96,98,74,65],
#     "Tup":("Apple","Banana","Mango"),
# }
# dict["Age"]=15
# dict["Name"]="Rajendhra prsad"
# print(dict)
# print(dict["Marks"])

# Nested Dictionary
info={
    "Name":"Rajendra parsad",
    "Subject":{
        "Phy":98,
        "Chem":95,
        "Maths":97,
        "Hindi":63,
    },
    "Tup":("Mukesh","Janvi","Rahul"),
}
# print(info["Subject"])
# print(info["Subject"]["Chem"])
# print(info)
print(info.keys())
print(info.values())
print(info.items())
print(info.update({"Cit`y":["Bikaner","Ajmer"]}))
print(info)