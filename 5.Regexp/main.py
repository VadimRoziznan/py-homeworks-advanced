import csv
import re


with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pattern = r"[-()\s]"
replace = ''
pattern_1 = r"(\+7|^8)(\d\d\d)(\d\d\d)(\d\d)(\d\d)"
replace_1 = r'+7(\2)\3-\4-\5'
replace_2 = r'+7(\2)\3-\4-\5 '
temporary_list = []
final_list = []

for index, item in enumerate(contacts_list):
    temporary_list.append((' ').join(item[0:3]).split(' ')[0:3])
    if contacts_list[index][3]:
        temporary_list[index].append(contacts_list[index][3])
    else:
        temporary_list[index].append('')
    if contacts_list[index][4]:
        temporary_list[index].append(contacts_list[index][4])
    else:
        temporary_list[index].append('')
    if contacts_list[index][5]:
        r = re.sub(pattern, replace, ''.join(contacts_list[index][5]))
        if 'доб.' in r:
            r = re.sub(pattern_1, replace_2, r)
        else:
            r = re.sub(pattern_1, replace_1, r)
        temporary_list[index].append(r)
    else:
        temporary_list[index].append('')
    if contacts_list[index][6]:
        temporary_list[index].append(contacts_list[index][6])
    else:
        temporary_list[index].append('')

for index in range(len(temporary_list)):
    for el in range(index+1, len(temporary_list)):
        if temporary_list[index][0] in temporary_list[el]:
            for k in range(len(temporary_list[index])):
                if temporary_list[index][k]:
                    continue
                else:
                    temporary_list[index][k] = temporary_list[el][k]
            temporary_list[el] = temporary_list[index]
    if temporary_list[index] not in final_list:
        final_list.append(temporary_list[index])

with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(final_list)
