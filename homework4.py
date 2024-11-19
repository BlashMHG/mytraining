#На вход даны следующие данные:
#Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
#Например: 'Aaron' - [5, 3, 3, 5, 4]
#Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
#Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.
#Вывод в консоль:
#{'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}
from platform import java_ver

from gc import get_freeze_count, get_threshold

from time import struct_time

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

grades = (sum(grades[0])/len(grades[0]),
          sum(grades[1])/len(grades[1]),
          sum(grades[2])/len(grades[2]),
          sum(grades[3])/len(grades[3]),
          sum(grades[4])/len(grades[4]))

students = list(sorted({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}))

#average = {students[0]: grades[0],
 #     students[1]: grades[1],
  #    students[2]: grades[2],
   #   students[3]: grades[3],
    #  students[4]: grades[4]}

average = dict(zip(students, grades))

print(average)


