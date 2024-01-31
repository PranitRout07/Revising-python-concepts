import csv
file = open('./qs.csv')
csvreader = csv.reader(file)
rows = []
for row in csvreader:
    rows.append(row)
ans = input("Do you want to complete this quiz? (yes/no) ")
if ans.lower()!="yes":
    print("You have exited quiz!!")
    exit(1)
i = 0
total_no_qs = len(rows)
total_no_correct_ans = 0
while i<total_no_qs:
    answer = input(rows[i][0])
    if answer.lower() == rows[i][1]:
        total_no_correct_ans+=1
        print("Correct!")
    else:
        print("Incorrect!")
    i +=1
print(f"You have got {(total_no_correct_ans/total_no_qs)*100}%")

