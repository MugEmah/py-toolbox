# STUDENT GRADE CLASSIFIER

student_name = input("Enter student name: ")

try:
    score = float(input("Enter student score (0 - 100): "))

    #Validate score range
    if score < 0 or score > 100:
        print("Error: Score must be btn 0 and 100.")

    else:
        if score >= 75:
            grade = "Distinction"
            result = "PASS"

        elif score >= 60:
            grade = "Merit"
            result = "PASS"

        elif score >= 50:
            grade = "Pass"
            result = "PASS"

        else:
            grade = "Fail"
            result = "FAIL"

        print(
            f"Student: {student_name} | "
            f"Score: {score:.1f} | "
            f"Grade: {grade} | "
            f"Result: {result}"
        )

except ValueError:
    print("Error: Please enter a valid numeric score.")