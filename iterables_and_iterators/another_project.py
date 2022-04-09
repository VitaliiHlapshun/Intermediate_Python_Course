from rooster import student_roster
import itertools


# Import modules above this line
class ClassroomOrganizer:
    def __init__(self):
        self.sorted_names = self.sort_alphabetically(student_roster)

    @staticmethod
    def sort_alphabetically(students):
        names = []
        for student_info in students:
            name = student_info['name']
            names.append(name)
        return sorted(names)

    def get_students_with_subject(self, subject):
        selected_students = []
        for student in student_roster:
            if student['favorite_subject'] == subject:
                selected_students.append({student['name'], subject})
        iterator = selected_students.__iter__()
        for i in iterator:
            print(i)
        # try:
        #     print(iterator.__next__())
        #     print(iterator.__next__())
        #     print(iterator.__next__())
        #     print(iterator.__next__())
        # except StopIteration as e:
        #     print("That's all...")


    def _desk_combibations(self):
        pass


classorg = ClassroomOrganizer()
classorg.get_students_with_subject('Math')
