"""Extra credit from CodeWars."""
from stack import Stack


def is_balanced(string):
    """Check if string of parenthesis is valid."""
    """Reverse string and use stack, in accordance with assignment."""
    rev = string[::-1]
    parens = Stack()

    for i in rev:
        parens.push(i)

    count = 0

    for i in range(parens.__len__()):
        p = parens.pop()

        if p == '(':
            count += 1
        elif p == ')':
            count -= 1

        if count < 0:
            break

    if count == 0:
        return 'balanced'
    elif count == 1:
        return 'open'
    else:
        return 'broken'


if __name__ == '__main__':
    """Main method."""
    parens = "())"
    balanced = is_balanced(parens)
    print(balanced)
