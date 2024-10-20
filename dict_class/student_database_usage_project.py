#Task1:Read excel using python and display data project wise:
#Task2 - Read data from excel and convert to dictionaries project wise
#student_dict={library:{csc_books:50,eee_books:100,.....},transport:{jubleehills: 10,.....},
# teaching_info:{csc_branch:200,.........}}

#importing package
import pandas as pd

#Reading excel
student_df=pd.read_excel("E:\\NaomTech\\student_database_usage.xlsx")
#print(type(student_df))

#dataframe - is like a table in python
#Extract porject details,folders,size

project_list=tuple(student_df['ProjectName'])
print(project_list)

folders_list=tuple(student_df['Folders'])
print(folders_list)

size_df=tuple(student_df['Size In GB'])
print(size_df)

#From this list,we should build a dictionary
student_dict=student_df.to_dict()
#print(student_dict)

# Convert the data to a dictionary
result = {}
for _, row in student_df.iterrows():
    project = row['ProjectName']
    folder_info = (row['Folders'],row['Size In GB'])

    if project not in result:
        result[project] = []

    result[project].append(folder_info)

# Output the resulting dictionary
print(result)





