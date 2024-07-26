'''
a. It creates a key;
b. Put the values on the key. 
'''
Student_ID = {"a" : "Al-Amin Kabir",
              "b" : "Tomal",
              "c" : "Sohan"
             }
print(Student_ID)
print(Student_ID["a"])
print(Student_ID.get("b"))
print(Student_ID.get("c","Oh no!"))
print(Student_ID.get("m","Oh no!"))