import re
import csv
from pprint import pprint



def names_create():
    for contact in contacts_list[1:]:
        line = contact[0] + ' ' + contact[1] + ' ' + contact[2]
        if len(line.split()) == 3:
            contact[0] = line.split()[0]
            contact[1] = line.split()[1]
            contact[2] = line.split()[2]
        elif len(line.split()) == 2:
            contact[0] = line.split()[0]
            contact[1] = line.split()[1]
            contact[2] = ''
        else:
            contact[0] = line.split()[0]
            contact[1] = ''
            contact[2] = ''
        contact[5] = phone_number_format(contact)

    return


def phone_number_format(contact):
    phone_pattern = re.compile(
        r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    phone_substitution = r'+7(\2)\3-\4-\5\7\8\9'
    col= phone_pattern.sub(phone_substitution, contact[5])
    return (col)


def duplicate_fill():
    for new in contacts_list:
        for raw in contacts_list:
            if new[0] + new[1] == raw[0] + raw[1]:
                if new[2] == '':
                    new[2] = raw[2]
                if new[3] == '':
                    new[3] = raw[3]
                if new[4] == '':
                    new[4] = raw[4]
                if new[5] == '':
                    new[5] = raw[5]
                if new[6] == '':
                    new[6] = raw[6]

def create_unique():
    new_list.append(contacts_list[0])
    for cont in contacts_list[1:]:
        for new in new_list:
            if cont[0]+ cont[1] != new[0]+new[1]:
                pr = 1
            else:
                pr = 0
                break
        if pr == 1:
            new_list.append(cont)



if __name__ == '__main__':
    with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        new_list=[]
        names_create()
        duplicate_fill()
        create_unique()
        pprint(new_list)

    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_list)
