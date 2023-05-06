from course import Course
from courselist import CourseList


def main():
    with open("data.txt") as data_f:
        data_l = [x.strip().split(",") for x in data_f.readlines()]
    course_list = CourseList()
    for i in data_l:
        current_c = Course(course_number=int(i[0]), course_name=i[1], credit_hrs=float(i[2]), grades=float(i[3]))
        course_list.insert(current_c)

    print()
    print(f"Current List: ({course_list.size()})")
    print(course_list)
    print()
    gpa = course_list.calculate_gpa()
    print(f"Cumulative GPA: {gpa:.3f}")
    print()

if __name__ == "__main__":
    main()
