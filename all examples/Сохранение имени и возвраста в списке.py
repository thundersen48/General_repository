'''
3
John
Maks 18
Ivan 30
'''
people = []
n = int(input())
for i in range(n):
    person = input()
    print(person.split(" "))
    # name, age = person.split(' ')
    lst = person.split(" ")
    name, age = person.split(' ')
    person_tuple = (name, int(age))
    people.append(person_tuple)
print(people)
