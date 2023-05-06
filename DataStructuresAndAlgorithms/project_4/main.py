from stack import Stack
from stack_object import StackObject


def eval_postfix(expr):
    """takes expression and returns calculation as float"""
    if not isinstance(expr, str):
        raise ValueError
    expr = expr.replace(" ", "")
    if len(expr) == 1:
        return float(expr)
    elif len(expr) % 2 == 0:
        raise SyntaxError(f"{expr}")
    stack = Stack()

    for i in range(len(expr)):
        if expr[i] == "+":
            value1 = stack.pop(obj_type=True)
            value2 = stack.pop(obj_type=True)
            result = float(value2.get_item()) + float(value1.get_item())
            stack.push(result)

        elif expr[i] == "-":
            value1 = stack.pop(obj_type=True)
            value2 = stack.pop(obj_type=True)
            result = float(value2.get_item()) - float(value1.get_item())
            stack.push(result)

        elif expr[i] == "*":
            value1 = stack.pop(obj_type=True)
            value2 = stack.pop(obj_type=True)
            result = float(value2.get_item()) * float(value1.get_item())
            stack.push(result)

        elif expr[i] == "/":
            value1 = stack.pop(obj_type=True)
            value2 = stack.pop(obj_type=True)
            result = float(value2.get_item()) / float(value1.get_item())
            stack.push(result)

        else:
            stack.push(expr[i].strip())

    return stack.pop(obj_type=True).get_item()


def in2post(expr):
    """takes infix expression and returns postfix as string

    arguments:
    expr -- type string
    """
    if not isinstance(expr, str):
        raise ValueError
    elif len(expr) % 2 == 0:
        raise SyntaxError(f"{expr}")

    stack = Stack()
    result = ""

    for i in range(len(expr)):
        if expr[i] == "(":
            # add to stack with priority 0
            stack.push(expr[i].strip())
            item = stack.top(obj_type=True)
            item.set_priority(0)

        elif expr[i] == ")":
            # add to stack with priority 3
            item = StackObject(expr[i].strip())
            item.set_priority(0)

            while stack.size() > 0 \
                    and stack.top(obj_type=True).get_priority() >= item.get_priority():
                if stack.top(obj_type=True).get_priority() == 0:
                    stack.pop(obj_type=True)
                    break
                result += stack.pop(obj_type=True).get_item()

        elif expr[i] == "+" or expr[i] == "-" or expr[i] == "*" or expr[i] == "/":
            item = StackObject(expr[i].strip())
            if expr[i] == "+" or expr[i] == "-":
                # priority 1
                item.set_priority(1)

            else:
                # priority 2
                item.set_priority(2)

            while stack.size() > 0 and stack.top(obj_type=True).get_priority() != 0 \
                    and stack.top(obj_type=True).get_priority() >= item.get_priority():
                result += stack.pop(obj_type=True).get_item()

            stack.push(item.get_item())
            if expr[i] == "+" or expr[i] == "-":
                # priority 1
                stack.top(obj_type=True).set_priority(1)

            else:
                # priority 2
                stack.top(obj_type=True).set_priority(2)

        else:
            # store value in result
            result += expr[i].strip()

    if stack.size() > 0 and stack.top(obj_type=True).get_priority() != 0:
        result += stack.pop(obj_type=True).get_item()

    return result


def main():
    with open("data.txt") as DATA_FILE:
        data_list = [x.strip() for x in DATA_FILE.readlines()]

    for i in data_list:
        # write to outfile
        print(f"infix: {i}")
        postfix = in2post(i)
        print(f"postfix: {postfix}")
        print(f"answer: {eval_postfix(postfix)}\n")

    with open("out.txt", "w") as OUT_FILE:
        for i in data_list:
            # write to outfile
            OUT_FILE.write(f"infix: {i}\n")
            postfix = in2post(i)
            OUT_FILE.write(f"postfix: {postfix}\n")
            OUT_FILE.write(f"answer: {eval_postfix(postfix)}\n\n")

if __name__ == "__main__":
    main()
