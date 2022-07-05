from itertools import takewhile, dropwhile
import sys

# (Trigger, Active, Word, Delete above, Before, Reverse
rules = [
    (3, False, "Fizz", False, "?", False),
    (5, False, "Buzz", False, "?", False),
    (7, False, "Bang", False, "?", False),
    (11, False, "Bong", True, "?", False),
    (13, False, "Fezz", False, "B", False),
    (17, False, "", False, "?", True)
]

def outputString(n):
    output = []
    for rule in filter(lambda x: x[1], rules):
        # Trigger
        if n % rule[0] == 0:
            # Delete above
            if rule[3]:
                output = []

            # Place correctly
            if(rule[4] != "?"):
                # Python is awful
                output = (list(takewhile(lambda x: x[0] != rule[4], output))) + [rule[2]] + (list(dropwhile(lambda x: x[0] != rule[4], output)))
            else:
                if rule[2] != "":
                    output.append(rule[2])

            # Reverse
            if(rule[5]):
                output.reverse()

    if output == []:
        output = str(n)
    else:
        output = "".join(output)

    return output


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    max = int(sys.argv[1])

    for j in range(2, len(sys.argv)):
        for rule in range(0, len(rules)):
            if int(sys.argv[j]) == rules[rule][0]:
                rules[rule] = rules[rule][0:1] + (True,) + rules[rule][2:]


    for i in range(1, max):
       print(outputString(i))

# Hi!