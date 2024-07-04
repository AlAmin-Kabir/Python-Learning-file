subjects = ["C","C++","Java","Python"]
 #Print_all_elements
print(subjects)
#Print from specific point(Ex-2)
print(subjects[2:])
#Print reverse
print(subjects[:-1])
#Search if an elements is inside the list or not
print("Python" in subjects)
#List related functions
#1. List length
print(len(subjects))
#2. List length from specific point
print(len(subjects[2:]))
#3. Attach another item to list
subjects.append("Al-Amin")
print(subjects)
'''4. Attach from any point(using insert function)
 insert(index,Object)'''
subjects.insert(2,"Disha")
print(subjects)
'''5. Remove from any point(using remove function)
 remove(Object)'''
subjects.remove("Disha")
subjects.remove("Al-Amin ")
print(subjects)

