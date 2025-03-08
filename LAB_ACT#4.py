def assign_grade(score):
    if score < 0 or score > 100:
        print("Bawal yan boss.")
    else:
        if score >= 90:
            print("Grade: A")
        elif score >= 80:
            print("Grade: B")
        elif score >= 70:
            print("Grade: C")
        elif score >= 60:
            print("Grade: D")
        elif score <= 60:
            print("Grade F")