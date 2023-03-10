from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    pattern = r"(\s+'',)/(\')"
    replace = r""

    r = []
    for el in contacts_list:

        r.append(re.sub(pattern, replace, ' '.join(el)))

    pprint(r)


