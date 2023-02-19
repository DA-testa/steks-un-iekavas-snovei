# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            # Process closing bracket
            if not opening_brackets_stack:
                return i +1
            top - opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return i + 1

    if opening_brackets_stack:
        top = opening_brackets_stack.pop()
        return top.position + 1

    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer
    print(mismatch)


if __name__ == "__main__":
    main()
