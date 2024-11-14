#Create a list of city names  add 8 elements in it and perform CRUD operation on it
cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", 
          "Kolkata", "Pune", "Hyderabad", "Ahmedabad"]
print(cities)

print("----")#read
print("\nReading City at index 2:", cities[2])

print("----")#update
cities[3] = "Jaipur"
print(cities)

print("----")#delete
cities.remove("Mumbai")
print(cities)

print("----")#insert
cities.append("Surat")
print(cities)
print("-------------------------------------------------------------------------------")
#Create a mixed list and change the value of third index to another data type value
mixed_list = [25, "Apple", 3.14, True, "Mumbai"]
print("first list",mixed_list)

print("----")#change value
mixed_list[3] = "Hii"
print("changed list",mixed_list)
print("-------------------------------------------------------------------------------")
#Create a list of Countries name , reverse the list and print only middle elements from the list
countries = ["India", "USA", "Canada", "Australia", "Germany", "Japan", "Brazil", "France"]
print("first list",countries)
countries.reverse()
print("Reversed List:", countries)
mid_index = len(countries) // 2
middle_elements = countries[mid_index - 1:mid_index + 1]
print("Middle Elements:", middle_elements)
print("-------------------------------------------------------------------------------")
#Create a list of pin-codes , delete the last pincode and the user required pincode from the list
pin_codes = [110001, 400001, 560001, 600001, 700001, 411001]
print("Original List of Pin-codes:", pin_codes)
pin_codes.pop()
print("After Deleting Last Pin-code:", pin_codes)
user_pin = int(input("Enter the pin-code to delete: "))
if user_pin in pin_codes:
    pin_codes.remove(user_pin)
    print(f"After Deleting {user_pin}:", pin_codes)
else:
    print(f"{user_pin} not found in the list.")
print("-------------------------------------------------------------------------------")
#Create a list of studentsName and perform all the pre-defined method and operation on it
students = ["Afrin", "seema", "riya", "mohinee", "anchal"]
print("Original List:", students)
students.append("Frank")
print("\nAfter Append:", students)
students.insert(2, "maha")
print("After Insert:", students)
students.remove("anchal")
print("After Remove:", students)
last_student = students.pop()
print(f"After Pop (Removed '{last_student}'):", students)
index_of_riya = students.index("riya")
print(f"Index of 'riya': {index_of_riya}")
count_of_riya = students.count("riya")
print(f"Count of 'riya': {count_of_riya}")
students.sort()
print("After Sort:", students)
students.reverse()
print("After Reverse:", students)
students.clear()
print("After Clear:", students)
