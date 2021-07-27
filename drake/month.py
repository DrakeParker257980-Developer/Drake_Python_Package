def daysinmonth():
    a = str(input("Enter The Name Of The Month => "))
    if "april" in a or "april" in a or "june" in a or "June" in a or "september" in a or "September" in a or "november" in a or "November" in a:
        print(f"In {a} There are 30 Days.")
    elif "february" in a or "February" in a:
        print(f"In {a} There are 28 Days But In a Leap Year there Are 29 Days .")
    elif "january" in a or "January" in a or "march" in a or "March" in a or "may" in a or "May" in a or "july" in a or "July" in a or "august" in a or "August" in a or "october" in a or "October" in a or "december" in a or "December" in a:
        print(f"In {a} There are 31 Days.")
    else:
        print("Invalid Month Name")