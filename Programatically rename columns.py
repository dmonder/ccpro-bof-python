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
#this line looks for more funkyness in the column names
stc.columns = stc.columns.str.replace(r"\s|Stc\s?|X\sSec\s?|Scs\s?|X\sScs\s?","")
#this addes a prefix to the column names
stc = stc.add_prefix('scs_')

#this looks for all columns with the word data and casts them to the object date_cols
date_cols = [col for col in stc.columns if 'Date' in col]

#this turns the columns into actual dates vs. txt formated values.
stc[date_cols]=stc[date_cols].apply(pd.to_datetime)

'''Next, we want to retain data from one row to the next where the current row is blank - same idea as LAG.
  one would think we would want to simply name the columns by name.  However, we actually dont'e know the 
  names of the columns, we just know their location.  Thus, we use the iloc method'''

retained = [0,1,2,3,4,5,6,7,8,9]

for retain in retained:
    scs1.iloc[:,retain].fillna(method='pad', inplace=True)
