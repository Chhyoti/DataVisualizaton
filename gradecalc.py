
def myGrade(grades):
    return sum(grades)  /len(grades)
def highestNumber(grades):
    return max(grades)
def lowestNumb(grades):
    return min(grades)

def main():
    grades = [45,67,89,90,56]

    # to calculate average grade
    avg_grade = myGrade(grades)

    # highest grade 
    highest = highestNumber(grades)

    # lowest grade 
    lowest = lowestNumb(grades)

    print(f"Grades: {grades}")
    print("Avg grade is",avg_grade)
    print(highest)
    print(lowest)


if __name__ == "__main__":
    main()
 