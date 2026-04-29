import json

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data,f, indent=4, ensure_ascii=False)


def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def add_student(students, next_id):
    name = input("name: ").strip()
    class_name = input("class name: ").strip()
    subject = input("subject: ").strip()
    score_input = input("score: ").strip()
    if score_input.isdigit():
        score = int(score_input)
    else:
        print("invalid score!")
        return next_id
    
    if any(s["name"].lower() == name.lower() and s["class"].lower() == class_name.lower() for s in students):
        print("student already exists!")
        return next_id
    
    student = {
        "id": next_id,
        "name": name,
        "class": class_name,
            "scores": {
                subject: score
            }
    }
    students.append(student)
    print("student added!")
    return next_id + 1


def show_students(students):
    if not students:
        print("no student found!")
        return
    
    for s in students:
        print(f"id: {s['id']} | name: {s['name']} | class_name: {s['class']}")

        for subject, score in s["scores"].items():
                print(f"   {subject}: {score}")


def search_student(students):
    choice = input("search by (1=id, 2=name): ")

    if choice == "1":
        student_id = input("enter id: ")

        if student_id.isdigit():
            student_id = int(student_id)
        else:
            print("invalid id!")
            return
        
        for s in students:
            if s["id"] == student_id:
                print(f"id: {s['id']} | name: {s['name']} | class: {s['class']}")
                for subject, score in s["scores"].items():
                    print(f"   {subject}: {score}")
                return
            
        print("no student found!")

    elif choice == "2":
        name = input("enter name: ")

        for s in students:
            if s["name"].lower() == name.lower():
                print(f"id: {s['id']} | name: {s['name']} | class: {s['class']}")
                for subject, score in s["scores"].items():
                    print(f"   {subject}: {score}")
                return
        print("no student found!")

    else:
        print("invalid choice!")


def delete_student(students):
    if not students:
        print("no student found!")
        return
    
    show_students(students)
    name = input("enter student's name to remove: ")

    for i, s in enumerate(students):
        if s["name"].lower() == name.lower():
            removed = students.pop(i)
            print(f"{removed['name']} removed successfully!")
            return
        
    print("no student found!")


def add_score(students):
    if not students:
        print("no student found!")
        return    

    name = input("enter student's name to add score: ")
    new_subject = input("name subject: ")
    new_score = input("score: ")

    if new_score.isdigit():
        score = int(new_score)
    else:
        print("invalid score!")
        return

    for s in students:
        if s["name"].lower() == name.lower():
            s["scores"][new_subject] = score
            print("score added!")
            return

    print("no student found!")


def show_scores(students):
    if not students:
        print("no student found!")
        return
    
    name = input("enter student's name: ")

    for s in students:
        if s["name"].lower() == name.lower():

            if not s["scores"]:
                print("no score found!")
                return
            
            print(f"id: {s['id']} | name: {s['name']} |class: {s['class']}")
            for subject, score in s["scores"].items():
                print(f"   {subject}: {score}")
            return
            
    print("no student found!")


def show_average_all(students):
    if not students:
        print("no student found!")
        return
    
    for s in students:
        if not s["scores"]:
            print(f"{s['name']}: no scores")
            continue

        scores = s["scores"].values()
        average = sum(scores) / len(scores)

        print(f"{s['name']}'s average: {average:.1f}")
        

def show_average_one(students):
    if not students:
        print("no student found!")
        return
    
    show_students(students)
    name = input("enter student's name to show average: ").strip()

    for s in students:
        if s["name"].lower() == name.lower():

            if not s["scores"]:
                print(f"{s['name']}: no score")
                return
            
            scores = s["scores"].values()
            average = sum(scores) / len(scores)

            print(f"{s['name']}'s average: {average:.1f}")
            return
        
    print("no student found!")


def update_score(students):
    if not students:
        print("no student found!")
        return
    
    name = input("enter student's name: ")

    for s in students:
        if s["name"].lower() == name.lower():

            if not s["scores"]:
                print("no score found!")
                return
            
            for subject, score in s["scores"].items():
                print(f"{subject}: {score}")

            subject = input("enter subject name to update: ")

            if subject in s["scores"]:
                score_input = input("new score: ")

                if not score_input.isdigit():
                    print("invalid score!")
                    return
                
                s["scores"][subject] = int(score_input)
                print("updated!")
                return
            
            print("no subject found!")
            return
        
    print("no student found!")


def delete_score(students):
    if not students:
        print("no student found!")
        return
    
    show_students(students)
    name = input("enter student's name: ")

    for s in students:
        if s["name"].lower() == name.lower():

            if not s["scores"]:
                print("no score found!")
                return
            
            print(s["scores"])

            subject = input("enter subject name to remove: ")

            if subject not in s["scores"]:
                print("no subject found!")
                return
            
            del s["scores"][subject]
            print("removed!")
            return
    print("no student found!")


# main program

students = load_data()

if students:
    next_id = max(s["id"] for s in students) + 1
else:
    next_id = 1

while True:

    print("\n=== student's scores manager ===")
    print("1. add student")
    print("2. show students")
    print("3. search student")
    print("4. delete student")
    print("5. add score")
    print("6. show scores")
    print("7. show average all")
    print("8. show average one")
    print("9. update score")
    print("10. delete score")
    print("11. exit")

    choice = input("choose: ").strip()

    if choice == "1":
        next_id = add_student(students, next_id)
        save_data(students)

    elif choice == "2":
        show_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        delete_student(students)
        save_data(students)

    elif choice == "5":
        add_score(students)
        save_data(students)

    elif choice == "6":
        show_scores(students)

    elif choice == "7":
        show_average_all(students)

    elif choice == "8":
        show_average_one(students)

    elif choice == "9":
        update_score(students)
        save_data(students)

    elif choice == "10":
        delete_score(students)
        save_data(students)

    elif choice == "11":
        print("ended!")
        break

    else:
        print("invalid choice!")
        