class_python=['Mounika','Kiran','Praveen','Benson']
class_webapplication=['Kiran','Benson','Rachana','Suhas']
common=list(set(class_python).intersection(set(class_webapplication)))
print('Common students in both classes')
print(common)
total=list(set(class_python).union(set(class_webapplication)))
unique=list(set(total).difference(set(common)))
print('Unique students in both classes')
print(unique)