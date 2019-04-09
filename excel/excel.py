import openpyxl

wb = openpyxl.load_workbook('students.xlsx')

print(wb.sheetnames)

sheet_1 = wb.active

# for i in range(1, sheet_1.max_row):
# print(sheet_1.cell(row=i, column=2).value)

# ищу группы
groups_list = []
groups_id = []
prevGroup = []
data = sheet_1.cell(row=2, column=3).value
for i in range(2, sheet_1.max_row):
        if str(sheet_1.cell(row=i, column=3).value) not in groups_list:
                groups_list.append(str(sheet_1.cell(row=i, column=3).value))
                groups_id.append(i)

print(groups_list)
print(groups_id)

ws1 = wb.create_sheet("5.01")
ws2 = wb.create_sheet("5.02")
ws3 = wb.create_sheet("5.03")
for i in range(1,7):
    ws1.cell(row=1, column=i).value = sheet_1.cell(row=1, column=i).value
for i in range(1,7):
    ws2.cell(row=1, column=i).value = sheet_1.cell(row=1, column=i).value
for i in range(1,7):
    ws3.cell(row=1, column=i).value = sheet_1.cell(row=1, column=i).value

wb.save("students_edit.xlsx")
for i in range(2,groups_id[1]-1):
    ws1.cell(row=i, column=1).value = i-1



for i in range(1,int(groups_id[1])-1):
    for j in range(2,7):
        ws1.cell(row=i, column=j).value = sheet_1.cell(row=i, column=j).value
wb.save("students_edit.xlsx")

for i in range(2,groups_id[1]-1):
    ws2.cell(row=i, column=1).value = i-1


for i in range(int(groups_id[1]),int(groups_id[2])):
    for j in range(2,7):
        ws2.cell(row=i-6, column=j).value = sheet_1.cell(row=i, column=j).value
wb.save("students_edit.xlsx")

for i in range(2,groups_id[1]-1):
    ws3.cell(row=i, column=1).value = i-1

for i in range(int(groups_id[2]), sheet_1.max_row):
        for j in range(2, 7):
            ws3.cell(row=i - 11, column=j).value = sheet_1.cell(row=i, column=j).value


ws1.cell(row= 1, column=7).value = "Mark"
ws2.cell(row= 1, column=7).value = "Mark"
ws3.cell(row= 1, column=7).value = "Mark"



wb.save("students_edit.xlsx")