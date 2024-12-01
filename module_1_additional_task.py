grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_of_students = list(students)
list_of_students.sort()

average_score = {list_of_students[0]:float(sum(grades[0]))/float(len(grades[0]))}
average_score.update({list_of_students[1]:float(sum(grades[1]))/float(len(grades[1])),
                      list_of_students[2]:float(sum(grades[2]))/float(len(grades[2])),
                      list_of_students[3]:float(sum(grades[3]))/float(len(grades[3])),
                      list_of_students[4]:float(sum(grades[4]))/float(len(grades[4]))})
print(average_score)



