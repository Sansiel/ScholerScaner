# Import `load_workbook` module from `openpyxl`
from statistics import mean

from openpyxl import load_workbook
from openpyxl.utils import column_index_from_string, get_column_letter

from date_mark.not_db_models import GradeModel, SubjectModel, StudentModel, DateModel


class ImportService:
    import_file_path = 'date_mark/input/'
    format_input = '.xlsx'

    def import_data(self, filename) -> GradeModel:
        path = self.import_file_path + filename + self.format_input

        # Load in the workbooks
        wb = load_workbook(path)

        # Get a sheet by name
        sheet = wb.get_sheet_by_name(filename)
        classname = sheet['A7'].value.lower().split(': ')[1]
        grade_model = GradeModel(name=classname, subjects=[])
        year = sheet['A5'].value.split('Учебный год: ')[1].lower().split('/')[0]

        subject_model = []

        for i in range(2, 2000):
            column_index = column_index_from_string('A')
            student_number = str(sheet[get_column_letter(column_index) + str(i)].value)

            if 'Предмет:' in student_number:
                subject_name = student_number.split('Предмет:')[1].lower().split('/' + classname)
                subject_model = SubjectModel(name=subject_name[0] + subject_name[1])

            student_count = 0
            date_count = 3
            if student_number == "№":
                j = i + 2
                while sheet["A" + str(j)].value:
                    j += 1
                student_count = j - i  # 1 лишний раз, а 2 прибавленные в начале учтены позже

                while sheet[get_column_letter(date_count) + str(i + 1)].value:
                    date_count += 1

                for j in range(i + 2, i + student_count):
                    student_model = StudentModel(name=sheet['B' + str(j)].value)

                    month = ''
                    for d in range(3, date_count):
                        degree = sheet[get_column_letter(d) + str(j)].value
                        day = sheet[get_column_letter(d) + str(i + 1)].value
                        month_may = sheet[get_column_letter(d) + str(i)].value
                        if month_may:
                            month = month_may
                        if day.isdigit():
                            type_of_work_temp = sheet[get_column_letter(5) + str(i + student_count + 2 + d)].value
                            date = sheet[get_column_letter(1) + str(i + student_count + 2 + d)].value
                            theme = sheet[get_column_letter(2) + str(i + student_count + 2 + d)].value
                            date_model = DateModel(degree=degree, day=day, month=month, theme=theme,
                                                   type_of_work=type_of_work_temp, date=date)
                        else:
                            date_model = DateModel(degree=degree, day=day, month=month, theme='Итоговая',
                                                   type_of_work='Итоговая', date=day)
                        date_model.year = year
                        student_model.dates.append(date_model)
                    subject_model.students.append(student_model)
                grade_model.subjects.append(subject_model)
        return grade_model

    def get_recommend(self, filename: str) -> str:
        grade_model = self.import_data(filename)
        response = '<h1>-------------------' + grade_model.name + '-------------------</h1>\n'
        for subject_model in grade_model.subjects:
            response += '<h2>' + subject_model.subject_name + ':</h2>\n'
            for student_model in subject_model.students:
                # response += self.grade_trend(student_model)
                response += self.theme_not_understand(student_model)

        return response

    def grade_trend(self, student_model: StudentModel) -> str:
        degree_list = []
        for date_model in student_model.dates:
            if self.check_int(date_model.degree):
                degree_list.append(int(date_model.degree))
        trend = self.linreg(degree_list)
        if trend > 0.5:
            return '   у ' + student_model.fullname + ' наблюдается <strong>повышение</strong> успеваемости\n'
        if trend < 0.5:
            return '   у ' + student_model.fullname + ' наблюдается <strong>понижение</strong> успеваемости\n'
        return ''

    def theme_not_understand(self, student_model: StudentModel) -> str:
        # avg_degree = self.avg_degree(student_model.dates)
        avg_degree_now = []
        response = ''
        for date_model in student_model.dates:
            if self.check_int(date_model.degree):
                avg_degree_now.append(int(date_model.degree))
                if int(round(mean(avg_degree_now), 0)) > int(date_model.degree):
                    response += f'''\n{date_model.date} {date_model.theme} по причине {date_model.type_of_work}'''
        if response:
            return f'\nУ <strong>{student_model.fullname}</strong> наблюдаются проблемы в следующих темах: ' + response
        return ''

    def avg_degree(self, dates: list) -> float:
        degree_count = 0
        degree_sum = 0
        for date_model in dates:
            if self.check_int(date_model.degree):
                degree_count += 1
                degree_sum += int(date_model.degree)
        return degree_sum/degree_count


    def check_int(self, s):
        if not s:
            return False
        if s[0] in ('-', '+'):
            return s[1:].isdigit()
        return s.isdigit()

    def linreg(self, x_list) -> float:
        # avg_x = sum(x_list)/len(x_list)
        trends_list = []
        x_last = x_list[0]
        for x in x_list:
            if x > x_last:
                trends_list.append(1)
            if x < x_last:
                trends_list.append(0)
            x_last = x
        if len(trends_list) == 0:
            return 0.5
        return sum(trends_list) / len(trends_list)
