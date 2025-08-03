import numpy as np

# Data
Jhon = {"Maths":92,"Science":90,"Geography":82,"English":80}
Karen = {"Maths":100,"Science":92,"Geography":85,"English":81}
Lisa = {"Maths":89,"Science":82,"Geography":99,"English":72}
Kevin = {"Maths":90,"Science":81,"Geography":85,"English":93}

# Converting the data to NumPy arrays
Jhon_arr_values = np.array(list(Jhon.values()))
Karen_arr_values = np.array(list(Karen.values()))
Lisa_arr_values = np.array(list(Lisa.values()))
Kevin_arr_values = np.array(list(Kevin.values()))
print("Example NumPy array for Jhon's marks:", Jhon_arr_values)


# Computing the numpy arrays average 
def avg(n, axis=0):
    aver = np.sum(n, axis)/len(n)
    return aver

# Storing the Dictionary Values
def list_creator(arg):
    values = []
    for i in arg.values():
        values.append(i)
    return values

# Function to print the values
def marks_printer(name, arg, values):
    a = -1
    print(f"{name}'s Marks are:")
    for i in arg:
        a = a + 1
        print(f"{i}:{values[a]}")
    print(f"The average is: {avg(values)}\n")

# Printing the values
students = {
    "Jhon": Jhon,
    "Karen": Karen,
    "Lisa": Lisa,
    "Kevin": Kevin
}

for name, data in students.items():
    values = list_creator(data)
    marks_printer(name, data, values)

# Converting and printing the values to a 2D array
print("The Values converted to an 2D array looks like:\n")
arr = np.array([list_creator(Jhon), list_creator(Karen), list_creator(Lisa), list_creator(Kevin)])
print(arr)

# Subject wise mean of all students
arrm = np.mean(arr, axis=0)
subjects = np.array(list(Jhon.keys()))
print("\nThe mean of all the students in each subject is:\n")
for idx, i in enumerate(arrm):
    print(f"{subjects[idx]}: {i}")

