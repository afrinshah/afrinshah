#Write a Python program and calculate the mean of the below dictionary.
test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}
mean_value = sum(test_dict.values()) / len(test_dict)
print(mean_value)

print('---------------------------------------------------------------------')

#Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged_dict = {**dic1, **dic2, **dic3}
print(merged_dict)

print('---------------------------------------------------------------------')

#Write a Python program to get the key, value and item in a dictionary.
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for key, value in dict_num.items():
     print(f"Key: {key}, Value: {value}, Item: ({key}, {value})")

print('---------------------------------------------------------------------')

#Write a Python program to get the key, value and item in a dictionary
input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}
for key, value in input_dict.items():
    print(f"Key: {key}, Value: {value}, Item: ({key}, {value})")


    


     
    
