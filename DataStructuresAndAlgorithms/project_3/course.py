
class Course:
    """Creates a Course() with variables: course_number, course_name, credit_hrs, grades, next
    """

    def __init__(self, course_number: int = 0, course_name: str = "",
                 credit_hrs: float = 0.0, grades: float = 0.0):
        """inits Course object with pointer to None

        arguments:
        course_number -- type int (default 0)
        course_name -- type str (default "")
        credit_hrs -- type float (default 0.0)
        grades -- type float (default 0.0)
        """
        if isinstance(course_number, int) and course_number >= 0:
            self.course_number = course_number
        else:
            raise ValueError
        if isinstance(course_name, str):
            self.course_name = course_name
        else:
            raise ValueError
        if isinstance(credit_hrs, float) and credit_hrs >= 0:
            self.credit_hrs = credit_hrs
        else:
            raise ValueError
        if isinstance(grades, float) and grades >= 0:
            self.grades = grades
        else:
            raise ValueError

        self.next = None

    def number(self):
        """number() -- returns course_number as int"""
        return int(self.course_number)

    def name(self):
        """name() -- returns course_name as string"""
        return str(self.course_name)

    def credit_hr(self):
        """credit_hr() -- returns credit_hrs as float"""
        return float(self.credit_hrs)

    def grade(self):
        """grade() -- returns grades as float"""
        return float(self.grades)

    def set_next(self, node):
        """set_next(node) -- sets pointer to node
        arguments:
        node -- type Course()
        """
        self.next = node

    def get_next(self):
        """get_next() -- returns self.next"""
        return self.next

    def __str__(self):
        """returns string of Course as f"cs{course_number} {course_name} Grade: {grades} Credit Hours: {credit_hrs}"""
        return f"cs{self.course_number} {self.course_name} Grade: {self.grades:0.1f} " \
               f"Credit Hours: {self.credit_hrs:0.1f}"
