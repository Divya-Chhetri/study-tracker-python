def add_session(subject, hour):
    with open("studytracker.txt", "a") as file:
        file.write(subject + " - " + hour + "hrs\n")
    print("Session Added Successfully!")

def view_study_history():
    print("Your Session History--->>>")
    with open("studytracker.txt", "r") as file:
        session_history = file.read()
        return(session_history)

def total_study_hour():
    totals=0.0
    hrs=[]
    with open("studytracker.txt", "r") as file:
        for line in file:
            line=line.strip() #removes new line/extra space
            parts= line.split("-")
            hours_part=parts[1]
            hours=hours_part.replace("hrs","")
            # totals += float(hours)
            hours=float(hours) #sum of hours using list
            hrs.append(hours)
    totals = sum(hrs)
    return totals

def close_tracker():
    print("Study Tracker is Closed.....Bye Buddy!!!")

while True:
    print("=====Study Tracker=====")
    print("1. Add Study Session.")
    print("2. View Study History.")
    print("3. Total Study Hours.")
    print("4. Exit.")

    choice=input("Enter your choice: ")

    if choice=="1":
        subject = input("Enter subject:")
        hour = input("Enter hours:")
        add_session(subject, hour)

    elif choice=="2":
        history=view_study_history()
        print(history)

    elif choice=="3":
        total=total_study_hour()
        print("Total Study Hours: ", total)

    elif choice=="4":
        close_tracker()
        break

    else:
        print("Invalid Choice. Choose 1, 2, 3 or 4.")