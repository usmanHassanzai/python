lst = [1,2,3,4,4,5,6,7,8,4]

element = int(input("Which element you want to be search in list : "))
count_element = lst.count(element)

# if(count_element != 0):
#     print(f"Element {element} found {count_element} times.")

if(element in lst):
    print(f"Element {element} found {count_element} times.")
else:
    print(f"Element not found in list.")