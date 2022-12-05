# Import `load_workbook` module from `openpyxl`
from openpyxl import load_workbook
import xlwt


class ImportService:

    import_file_path = 'date_mark/input/'
    format_input = '.xlsx'

    def import_data(self, filename):
        path = self.import_file_path + filename + self.format_input

        path_class_import = self.import_file_path + filename + self.format_input
        path_class_output = self.import_file_path + filename + '.xls'

        # Load in the workbooks
        wb = load_workbook(path_class_import)
        wb_result = xlwt.Workbook(encoding="utf-8")

        # Get sheet names
        # print(wb.get_sheet_names())

        # Get a sheet by name
        sheet = wb.get_sheet_by_name(filename)
        sheet_result = wb_result.add_sheet(filename)
        sheet_result.write(0, 0, "Выставлены итоговые оценки 1 четверти/Триместра")
        sheet_result.write(0, 1, "Выставлены итоговые оценки 2 четверти")
        sheet_result.write(0, 2, "Оценка и Н в одной клетке")
        sheet_result.write(0, 3, "Накопляемость")
        sheet_result.write(0, 4, "Все темы")
        sheet_result.write(0, 5, "Домашки")

        sheet_result.col(0).width = 14000
        sheet_result.col(1).width = 14000
        sheet_result.col(2).width = 14000
        sheet_result.col(3).width = 14000
        sheet_result.col(4).width = 14000
        sheet_result.col(5).width = 14000

        # Work
        student_dictionary = []
        for i in range(30): student_dictionary.append(str(i + 1))
        quter1 = 3
        quter2 = 3

        i_quater1 = 1
        i_quater2 = 1
        i_ocenka = 1
        i_count = 1
        is_student = False
        a_counter = 1
        hw_counter = 1

        # if(sheet.cell(row=17,column=11).value=="Итог. 1 четв."):print("yes")
        # if(str(sheet["A" + str(48)].value)=="None"): print("Yes")
        # else: print(str(sheet["A" + str(48)].value))

        for i in range(2, 2000):
            student_number = str(sheet["A" + str(i)].value)

            if (student_number == "1"):
                check_quater1 = False
                check_quater2 = False
                check_ocenka = False
                check_count = False
                is_student = True

                checking_quater1 = False
                checking_quater2 = False

            if student_number in student_dictionary:

                # Заполнены все итоги 3 четверти
                if (checking_quater1):
                    pass
                else:
                    while (str(sheet.cell(row=(i - 1), column=quter1).value) != "Итог. 1 трим."):
                        quter1 += 1
                        if (str(sheet.cell(row=(i - 1), column=quter1).value) == "None"):
                            check_quater1 = True
                            checking_quater1 = True
                            break
                    checking_quater1 = True

                if (str(sheet.cell(row=i, column=quter1).value) == "None") and (is_student): check_quater1 = True

                # Заполнены все итоги 4 четверти
                if (checking_quater2):
                    pass
                else:
                    while (str(sheet.cell(row=(i - 1), column=quter2).value) != "Итог. 2 трим."):
                        quter2 += 1
                        if (str(sheet.cell(row=(i - 1), column=quter2).value) == "None"):
                            quter2 -= 1
                            check_quater2 = True
                            checking_quater2 = True
                            break
                    checking_quater2 = True

                if (str(sheet.cell(row=i, column=quter2).value) == "None") and (is_student): check_quater2 = True

                count = 0
                for j in range(3, quter2):
                    if (j == quter1) and (j == quter2):
                        pass
                    else:
                        # Оценка и Н в 1 месте
                        student_cell = str(sheet.cell(row=i, column=j).value)
                        if (len(student_cell) > 2):
                            for sc in student_cell.split(" "):
                                if (sc == "Н"): check_ocenka = True

                        # Накопляемость
                        if (student_cell != "None"): count = 0
                        if (student_cell == "None"): count += 1
                        if (count > 3): check_count = True

            if (is_student):
                if (student_number == "None"):
                    quter1 = 3
                    quter2 = 3

                    if (is_student):
                        is_student = False
                        teacher = str(sheet["A" + str(i + 2)].value)

                        if (check_quater1):
                            sheet_result.write(i_quater1, 0, teacher)
                            i_quater1 += 1

                        if (check_quater2):
                            sheet_result.write(i_quater2, 1, teacher)
                            i_quater2 += 1

                        if (check_ocenka):
                            sheet_result.write(i_ocenka, 2, teacher)
                            i_ocenka += 1

                        if (check_count):
                            sheet_result.write(i_count, 3, teacher)
                            i_count += 1

            if student_number == "Дата":
                s_teacher = str(sheet["A" + str(i - 2)].value)
                stoper_data = True

                while (True):
                    i += 1
                    student_number = str(sheet["A" + str(i)].value)
                    student_number2 = str(sheet["A" + str(i + 1)].value)

                    if (student_number != "None") and (student_number2 != "None"):
                        article_number = str(sheet["B" + str(i)].value)
                        homework_number = str(sheet["C" + str(i + 1)].value)

                        # Заполнены все темы
                        if (article_number == "None") and (stoper_data):
                            sheet_result.write(a_counter, 4, s_teacher)
                            a_counter += 1
                            stoper_data = False

                        # Заполнены все домашки
                        if (homework_number == "None") and (stoper_data):
                            sheet_result.write(hw_counter, 5, s_teacher)
                            hw_counter += 1
                            stoper_data = False

                    else:
                        break

        wb_result.save(path_class_output)