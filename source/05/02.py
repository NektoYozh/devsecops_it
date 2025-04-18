def print_list(list_name, items):
    print("{0}: ".format(list_name))
    for subject in items:
        print(subject)

school_subjects = ['mathematics', 'physics', 'chemistry', 'literature', 'biology', 'history']
print_list("School subjects", school_subjects)

answer = ''
while 1:
    while answer != 'yes' and answer != 'no':
        answer = input("Are there any subjects you don't like? (yes/no) ")
    if answer == 'no':
        print_list("School subjects", school_subjects)
        break
    else:
        dislike = input("What subject don't you like? ")
        if school_subjects.count(dislike) > 0:
            school_subjects.remove(dislike)
            print_list("School subjects", school_subjects)
        else:
            print("The list does not contain this item!")
        answer = input("Are there any subjects you don't like? (yes/no) ")







