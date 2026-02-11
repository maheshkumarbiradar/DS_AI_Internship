#task 1

import numpy as np
import pandas as pd
values = pd.Series(data = [700,150,300], index = ['Laptop', 'Mouse', 'Keyboard'])
print(values)
print("Laptop Price:", values['Laptop'])
print("First two prodacts:",values[0:2])

#Task 2

grades = pd.Series( [85, None, 92, 45, None, 78, 55])
grades.isnull()
grades.fillna(0)
print(grades[grades > 60])

#Task 3

usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
usernames.str.strip()
usernames.str.lower()
lw = usernames.str.lower()
lw.str.contains(('a'))
print(lw[lw.str.contains('a')])
