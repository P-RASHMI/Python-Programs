student = {'name':'Rashmi','hobbies':['dance','music']}
print(student)

student = {'name':'Rashmi','hobbies':['dance','music'],'java':{'jse':'netbeans','jee':'eclipse'}}
print(student['name'])
print(student['hobbies'])
print(student['java'])
student['phone'] ='53652735643572'
print(student)

student['name']='ravali'
print(student)

print(student.get('phone','7326837'))
