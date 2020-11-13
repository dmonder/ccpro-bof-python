import os
import pandas as pd

data_path = "M:/01_Python/01a_StudentCourseSec"

stc_fn = 'Warehouse2020FA 1A STUDENT.COURSE.SEC V1.csv'

# You don’t need to change directories to read the file
stc = pd.read_csv(os.path.join(data_path,stc_fn))

print(stc.columns)
# The Pythonic way to rename the columns is to do it like this.
# This uses a regular expression to find all whitespace characters (\s) or (the |)
# the sequence "Stc" possibly (the ?) followed by whitespace (\s) and delete them.
stc.columns = stc.columns.str.replace(r"\s|Stc\s?","")
print(stc.columns)
