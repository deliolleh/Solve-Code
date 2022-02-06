# Test Case
T = int(input())

# In Test Case
for i in range(T):
    # Get input
    letter = input()

    # Var Setting
    say = []
    say_nth = []
    result = []

    # Str => List
    for idx in range(len(letter)):
        say.append(letter[idx])

    # Make Repeat
    say_nth = say * 5

    # About First Person = > Pop odd letter
    say_a = say_nth[0::2]

    # Find Comeback index
    re_one = say_a[1:].index(say_a[0])

    # Collect Repeat letter
    for idx2 in range(re_one+1):
        result += say_a[idx2]

    # Print
    print(''.join(result))

    # Using Same Var, Clear it
    result.clear()

    # About Second Person => Same First
    say_b = say_nth[1::2]

    re_one = say_b[1:].index(say_b[0])

    for idx2 in range(re_one + 1):
        result += say_b[idx2]

    print(''.join(result))
