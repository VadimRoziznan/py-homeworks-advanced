from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


    pattern = r"('|\n)"
    replace = r""
    pattern_2 = r"\s+"
    replace_2 = r" "
    pattern_3 = re.compile(r"([А-ЯЁ][а-яё]*\s[А-ЯЁ][а-яё]*\s[А-ЯЁ][а-яё]*)|([А-ЯЁ][а-яё]*\s[А-ЯЁ]{1}[а-яё]*)")

    r = []
    names = []
    firstname = []
    surname = []

    for index, item in enumerate(contacts_list):

        r.append(re.sub(pattern, replace, ' '.join(contacts_list[index])))
        r[index] = re.sub(pattern_2, replace_2, r[index])
        if pattern_3.search(r[index]):
            f = pattern_3.search(r[index])
            names.append(f.group(0).split())
        r[index] = re.sub(pattern_3, '', r[index])
        print(r[index].split())
    # print(names)
    # print()
    # print()
    # print(r)



        # l = pattern_3.search(r[index])
        # print(l.group(0))


        # if r[index].split()[0:3][2][-3:] in ['вич', 'вна']:
        #     print(r[index].split()[0:3])





