from itertools import takewhile, dropwhile
import sys

class Rule:
    def __init__(self, trigger, active, word, deleteAbove, before, reverse):
        self.trigger = trigger
        self.active = active
        self.word = word
        self.deleteAbove = deleteAbove
        self.before = before
        self.reverse = reverse

# (Trigger, Active, Word, Delete above, Before, Reverse
### in what cases would be want these rules not to be active?
rules = [
    Rule(3, False, "Fizz", False, "?", False),
    Rule(5, False, "Buzz", False, "?", False),
    Rule(7, False, "Bang", False, "?", False),
    Rule(11, False, "Bong", True, "?", False),
    Rule(13, False, "Fezz", False, "B", False),
    Rule(17, False, "", False, "?", True)
]


def outputString(n):
    output = []
    for rule in filter(lambda x: x.active, rules):
        # Trigger
        if n % rule.trigger == 0:
            # Delete above
            if rule.deleteAbove:
                output = []

            ### see what you can do to make these comments more readable
            ### extention to that what can you do to your code to make it more readable that a comment isn't required?
            # Place correctly
            if(rule.before != "?"):
                # Python is awful
                output = (list(takewhile(lambda x: x[0] != rule.before, output))) + [rule.word] + (list(dropwhile(lambda x: x[0] != rule.before, output)))
            else:
                if rule.word != "":
                    output.append(rule.word)

            # Reverse
            if rule.reverse:
                output.reverse()

    if output == []:
        output = str(n)
    else:
        output = "".join(output)

    return output

### Should be able to run this without any additional commands at the start
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    max = int(sys.argv[1])
    
    ### Any extra rules or inputs should be requested from the user after the program has started running
    for j in range(2, len(sys.argv)):
        for rule in range(0, len(rules)):
            if int(sys.argv[j]) == rules[rule].trigger:
                rules[rule].active = True


    for i in range(0, max):
       print(outputString(i))
