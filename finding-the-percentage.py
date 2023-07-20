
n = int(input("enter n")) #kac not girilcek
student_marks = {}
for i in range(n):
    name, *line = input("enter the name and score").split() #isim
    scores = list(map(float, line)) #notlar
    student_marks[name] = scores
query_name = input("query name") #kimin ortalamasi lazim

if query_name in student_marks:
    scores_ = student_marks[query_name]
    average_ = sum(scores_) / len(scores_)
    print(average_)