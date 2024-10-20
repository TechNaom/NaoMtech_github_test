'''
Task1:Read excel using python and display data project wise:
Task2 - Read data from excel and convert to dictionaries project wise
student_dict={library:{csc_books:50,eee_books:100,.....},transport:{jubleehills: 10,.....},
teaching_info:{csc_branch:200,.........}}
Task3:Project - Total size of all
'''
from cProfile import label

#importing package
import pandas as pd
import matplotlib.pyplot as plot

from dict_class.dict_methods import color


#Extract porject details,folders,size
def getStduentDataColumWise(studentDF):
    try:
        project_list=tuple(student_df['ProjectName'])
        print(project_list)

        folders_list=tuple(student_df['Folders'])
        print(folders_list)

        size_df=tuple(student_df['Size In GB'])
        print(size_df)

        return project_list,folders_list,folders_list
    except Exception as ex:
        print(ex)
    return None

def convertStudenDataToDict(studentDF):
    student_dict={}
    # Convert the data to a dictionary
    for _,row in student_df.iterrows():
        projName=row['ProjectName']
        folderInfo=row['Folders']
        sizeInfo = row['Size In GB']

        if projName not in student_dict:
            student_dict[projName]=[]

        student_dict[projName].append((folderInfo,sizeInfo))
    #print(student_dict)
    return student_dict

'''
{'Library': [('csc_books', 50), ('eee_books', 100), ('it_books', 30), ('civil_books', 20),
 ('mech_books', 120), ('ai_books', 300)], 'Transport': [('jubleehills', 10), ('ameerpet', 200),
  ('kukatpally', 300), ('bhel', 40), ('hitechcity', 400)], 'Teaching_info': [('csc_branch', 200),
   ('eee_branch', 100), ('it_branch', 20), ('civil_branch', 30), ('mech_branch', 50), ('ai_branch', 400)]}
'''

#Task3:project wise sum of all folders
def getTotalProjectSizeDict(studentDict):
    project_size_dict={}

    #split dict by key and value
    for proj,folders_size in studentDict.items():
          total_size = 0
          for tup in folders_size:
              size=tup[1]
              total_size=total_size+size
          project_size_dict[proj]=total_size
    return project_size_dict

def generateStudentBarChart(projectSizeDict):
      #declare figure()
      #plot.figure(figsize=(8,6))

      # Iterarting for loop
      projectList=list(projectSizeDict.keys())
      print(projectList)
      sizeList=list(projectSizeDict.values())
      print(sizeList)
      bar_labels = ['Library', 'Transport', 'Teaching_info', 'sport', 'arts']
      bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange','tab:green']

      plot.figure(figsize=(8, 6))
      plot.bar(projectList,sizeList,label=bar_labels,color=bar_colors)
      for proj,size in zip(projectList,sizeList):
          plot.text(proj,size,size,fontsize=12)


      # Show the bar graph
      plot.show()


if __name__=='__main__':
    # Reading excel
    student_df = pd.read_excel("E:\\NaomTech\\student_database_usage.xlsx")
    print(student_df)
    #converting StudenData to a Dict
    studentDict=convertStudenDataToDict(student_df)
    print(studentDict)
    #Getting project wise size
    projectSizeDict=getTotalProjectSizeDict(studentDict)
    #Creating BarChart for student data
    print(projectSizeDict)
    #sort dict in descending.
    # dictionary sorted by value
    projectSizeDictSorted=dict(sorted(projectSizeDict.items(), key=lambda t: t[1],reverse=True))
    print(projectSizeDictSorted)
    generateStudentBarChart(projectSizeDictSorted)











