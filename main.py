import csv
import os

message1 = "こんにちは！私はRobokoです。あなたの名前は何ですか？"
message2 = "{}さん。どこのレストランが好きですか？"
message3 = "{}さん。ありがとうございました。\n" \
           "良い一日を！さようなら"

name = 'Taro'
# name = input()

print(message1)
print(message2.format(name))
print(message3.format(name))

name_count_list = [{'Name': 'A', 'Count': 1}, {'Name': 'B', 'Count': 2}]
print(name_count_list)

def add_name(name_count_list, name):
    for i in range(len(name_count_list)):
        if name_count_list[i]['Name'] == name:
            name_count_list[i]['Count'] += 1
            break
    if i == len(name_count_list) - 1:
        name_count_list.append({'Name': name, 'Count': 1})

add_name(name_count_list, 'A')
add_name(name_count_list, 'C')
add_name(name_count_list, 'D')
add_name(name_count_list, 'A')

print(name_count_list)

sorted_name_count_list = sorted(name_count_list, key=lambda person: person['Count'])
print(sorted_name_count_list)



with open('test.csv', 'w') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for person in sorted_name_count_list:
        writer.writerow(person)

if os.path.exists('test.csv'):
    with open('test.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        # d = {}
        for row in reader:
            print(row['Name'])
            print(row['Count'])






