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
    r = []
    for index, item in enumerate(contacts_list):

        r.append(re.sub(pattern, replace, ' '.join(contacts_list[index])))
        r[index] = re.sub(pattern_2, replace_2, r[index])
        # print(r[index].split()[0:2])
    pprint(r)

fvefv

