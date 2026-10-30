def main():
    print("STUDENT GRADE ANALYZER")

    while True:
        try:
            grade_count = int(input("How many grades would you like to enter? "))

            if grade_count > 0:
                break
            else:
                print("Please enter at least one grade.")

        except ValueError:
            print("Please enter a whole number.")

    grades = []

    for index in range(grade_count):
        while True:
            try:
                grade = float(input(f"Enter grade {index + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Please enter a grade from 0 to 100.")

            except ValueError:
                print("Please enter a valid number.")

    average = sum(grades) / len(grades)
    highest_grade = max(grades)
    lowest_grade = min(grades)

    if average >= 50:
        result = "PASS"
    else:
        result = "FAIL"

    print("\n===== RESULTS =====")
    print("Grades:", grades)
    print(f"Average: {average:.2f}")
    print(f"Highest Grade: {highest_grade:.2f}")
    print(f"Lowest Grade: {lowest_grade:.2f}")
    print("Status:", result)


if __name__ == "__main__":
    main()
