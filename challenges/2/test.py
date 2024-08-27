import main

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def test(input, expected_output):
    output = main.ohmsLaw(*input)
    if output == expected_output:
        print(f"{bcolors.OKGREEN}SUCCESS{bcolors.ENDC}: {input} -> {output}")
    else:
        print(f"{bcolors.FAIL}FAIL{bcolors.ENDC}: Test case '{input}': output should be '{expected_output}' but got '{output}'")


if __name__ == "__main__":
    test((12, 220, None), 0.05)
    test([230, None, 2], 115)
    test([None, 220, 0.02], 4.4)
    test([None, None, 2], "Invalid")
    test([None, None, None], "Invalid")
