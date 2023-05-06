
class CourseList:
    """Creates CourseList() with variables: head, cursor"""
    def __init__(self):
        """initiates object with variables: head, cursor set to None"""
        self.head = None
        self.cursor = None

    def insert(self, node):
        """insert(node) -- inserts node in CourseList() in course_number ascending order

        arguments:
        node -- type Course()
        """
        class_num = node.number()
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            next_node = current_node.next
            if next_node is None and class_num >= current_node.number():
                current_node.set_next(node)
                return
            elif next_node is None and class_num <= current_node.number():
                if current_node == self.head:
                    self.head = node
                    node.set_next(current_node)
                    return
            elif current_node.number() >= class_num:
                if current_node == self.head:
                    self.head = node
                    node.set_next(current_node)
                    return
            elif next_node.number() >= class_num:
                pointer = current_node.get_next()
                current_node.set_next(node)
                node.set_next(pointer)
                return

    def remove(self, number):
        """removes and returns first Course() with a course_number with the value of number
        """
        if self.head is None:
            return None
        else:
            for nodes in self:
                next_node = nodes.next
                if next_node is None:
                    if nodes.number() == number:
                        if nodes is self.head:
                            self.head = nodes.next
                        else:
                            if nodes.number() == number:
                                temp_node = nodes
                                nodes.set_next(None)
                                return temp_node
                elif next_node.number() == number:
                    if next_node.next is None:
                        nodes.set_next(None)
                        return next_node
                    else:
                        pointer = next_node.get_next()
                        nodes.set_next(pointer)
                        return next_node
                elif nodes.number() == number:
                    if nodes is self.head:
                        self.head = nodes.next
                    else:
                        if nodes.number() == number:
                            temp_node = nodes
                            nodes.set_next(None)
                            return temp_node

    def remove_all(self, number):
        """removes all Course() instances with a course_number with the value of number
        """
        if self.head is None:
            return None
        else:
            freq = 0
            for nodes in self:
                if nodes.number() == number:
                    freq += 1
            i = 0
            while i < freq:
                for nodes in self:
                    next_node = nodes.next
                    if next_node is None:
                        if nodes.number() == number:
                            if nodes is self.head:
                                self.head = nodes.next
                            else:
                                if nodes.number() == number:
                                    nodes.set_next(None)
                                    break
                    elif next_node.number() == number:
                        if next_node.next is None:
                            nodes.set_next(None)
                            break
                        else:
                            pointer = next_node.get_next()
                            nodes.set_next(pointer)
                            break
                    elif nodes.number() == number:
                        if nodes is self.head:
                            self.head = nodes.next
                        else:
                            if nodes.number() == number:
                                nodes.set_next(None)
                                break
                i += 1

    def find(self, number):
        """finds and returns first Course() with a course_number of number
        """
        if self.head is None:
            return -1
        for nodes in self:
            if nodes.number() == number:
                return nodes
        return -1

    def size(self):
        """returns the number of objects in CourseList() as int"""
        size = 0
        if self.head is None:
            return size
        for nodes in self:
            size += 1
        return size

    def calculate_gpa(self):
        """returns a float of a calculated gpa using grades weighted from the amount of credit hours"""
        w_list = []
        credit_list = []
        grade_total = 0
        credit_total = 0
        if self.head is None:
            return 0.0

        for nodes in self:
            grade_val = nodes.grade()
            credit_val = nodes.credit_hr()

            weighted_grade = grade_val * credit_val

            w_list.append(weighted_grade)
            credit_list.append(credit_val)

        for grades in w_list:
            grade_total += grades

        for credit_hrs in credit_list:
            credit_total += credit_hrs

        return grade_total/credit_total

    def is_sorted(self):
        """returns bool whether CourseList() is sorted"""
        for nodes in self:
            if nodes.next is not None:
                if nodes.number() > nodes.next.number():
                    return False
        return True

    def __str__(self):
        """returns string of CourseList
        """
        nodes = ""
        for node in self:
            nodes += f"{str(node)}\n"
        return nodes

    def __iter__(self):
        """points to the next object and returns the object in course list"""
        node = self.head
        while node is not None:
            yield node
            node = node.next
