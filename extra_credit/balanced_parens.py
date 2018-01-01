"""Extra credit from CodeWars."""


def is_balanced(parens):
    """Check if string of parenthesis is valid."""
    count = 0
    index = 0

    while index < len(parens):
        if parens[index] == '(':
            count += 1
        elif parens[index] == ')':
            count -= 1

        if count < 0:
            break

        index += 1

    if count == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    """Main method."""
    parens = "hi())("
    balanced = is_balanced(parens)
    print(balanced)
