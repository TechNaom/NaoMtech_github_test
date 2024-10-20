student_dict={'Library': 620, 'Transport': 950, 'Teaching_info': 800, 'sport': 600, 'arts': 800}

#bulit in sort
student_dict_sorted=sorted(student_dict.items(),key=lambda x:x[1:],reverse=True)
print(student_dict_sorted)

