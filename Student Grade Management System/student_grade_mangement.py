class StudentGradeManagement:

    def __init__(self, name):
        try:
            with open('student_grade.txt', 'r') as f:
                self.content = f.readlines()
                self.list_content = [line.strip().split(',') for line in self.content]
        except FileNotFoundError:
            print('Error: student grades file not found')
            self.list_content = []

        self.name = name
        teachers = ['rayan']

        if name in teachers:
            self.teachers_main()
        else:
            self.student_main()

    def student_main(self):
        print('1. You want to review your grades')
        print('2. You want to generate a report of your grades')

        try:
            choice = int(input('1/2: '))
        except ValueError:
            print('Error: you entered an invalid choice, try again')
            choice = int(input('1/2: '))

        if choice == 1:
            print('Ok, you want to see your grades')
            self.see_grade()
        elif choice == 2:
            print('Ok, we are generating a report of your grades')
            self.report_generator()
        else:
            print('You entered an invalid choice, try again')

    def report_generator(self):
        for student_data in self.list_content:
            if student_data[0] == self.name:
                print('We have found your name')
                marks_list = list(map(int, student_data[1:]))
                total_subjects = len(marks_list)
                marks_earned = sum(marks_list)

                percentage = marks_earned / total_subjects

                if percentage < 33:
                    print('Sorry, you have failed')
                    print(f'Total marks you earned: {marks_earned} and overall grade: F')

                    subjects = ['maths', 'english', 'Ilamiyat', 'Urdu', 'pak studies']
                    for index, mark in enumerate(marks_list):
                        if index < len(subjects):
                            print(f'{mark} out of 100 in {subjects[index]}')
                else:
                    print('You have passed')
                    if 33 <= percentage < 50:
                        grade = 'D'
                    elif 50 <= percentage < 60:
                        grade = 'C'
                    elif 60 <= percentage < 70:
                        grade = 'B'
                    elif 70 <= percentage < 80:
                        grade = 'A'
                    elif 80 <= percentage < 90:
                        grade = 'A'
                    elif percentage >= 90:
                        grade = 'A*'

                    print(f'Total marks you earned: {marks_earned} out of {total_subjects*100} and overall grade: {grade}')
                return

        print('We cannot generate a report for you as we do not have your name in the list. It seems you entered the wrong name. Try again.')

    def see_grade(self):
        subjects = ['maths', 'english', 'Ilamiyat', 'Urdu', 'pak studies']
        for student_data in self.list_content:
            if student_data[0] == self.name:
                print('Your grades are:')
                for index, mark in enumerate(student_data[1:]):
                    if index < len(subjects):
                        mark = int(mark)
                        grade = self.get_grade(mark)
                        print(f'{subjects[index]}: {grade}')
                return
        print('We do not have your grades. It seems you entered the wrong name.')

    def get_grade(self, mark):
        if mark >= 90:
            return 'A*'
        elif mark >= 80:
            return 'A'
        elif mark >= 70:
            return 'B'
        elif mark >= 60:
            return 'C'
        elif mark >= 50:
            return 'D'
        else:
            return 'F'

    def teachers_main(self):
        print('1. Enter student marks')
        print('2. Delete student marks')
        print('3. Update student marks')

        try:
            choice = int(input('1/2/3: '))
        except ValueError:
            print('Error: you entered an invalid choice, try again')
            choice = int(input('1/2/3: '))

        if choice == 1:
            self.add_marks()
        elif choice == 2:
            self.delete_marks()
        elif choice == 3:
            self.update_marks()
        else:
            print('You entered an invalid choice, try again')

    def add_marks(self):
        student_name = input('Enter the student name: ')

        marks = []
        subjects = ['maths', 'english', 'Ilamiyat', 'Urdu', 'pak studies']
        for subject in subjects:
            marks.append(input(f'Enter marks of {subject}: '))

        add_list = [student_name] + marks
        with open('student_grade.txt', 'a') as f:
            f.write(','.join(add_list) + '\n')

    def delete_marks(self):
        print('Which student marks do you want to delete? Enter the name: ')
        delete_name = input()

        self.list_content = [student_data for student_data in self.list_content if student_data[0] != delete_name]
        
        with open('student_grade.txt', 'w') as f:
            for student_data in self.list_content:
                f.write(','.join(student_data) + '\n')

        print('Deleted successfully' if any(student_data[0] == delete_name for student_data in self.list_content) else 'Name not found')

    def update_marks(self):
        print('Enter the name of the student whose marks you want to update: ')
        update_name = input()

        for student_data in self.list_content:
            if student_data[0] == update_name:
                marks = []
                subjects = ['maths', 'english', 'Ilamiyat', 'Urdu', 'pak studies']
                for subject in subjects:
                    marks.append(input(f'Enter new marks of {subject}: '))

                student_data[1:] = marks
                break

        with open('student_grade.txt', 'w') as f:
            for student_data in self.list_content:
                f.write(','.join(student_data) + '\n')

        print('Updated successfully')

# Example usage:
if __name__ == "__main__":
    name = input("Enter your name: ")
    student = StudentGradeManagement(name)