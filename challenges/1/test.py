import main

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def test(input, output):
    if main.capToFront(input) == output:
        print(f"{bcolors.OKGREEN}SUCCESS{bcolors.ENDC}: {input}")
    else:
        print(f"{bcolors.FAIL}FAIL{bcolors.ENDC}: Test case '{input}': output should be '{output}' but got '{main.capToFront(input)}'")


if __name__ == "__main__":
    test("HelloB", "HBello")
    test("test", "test")
    test("ALL", "ALL")
    test("hApPy", "APhpy")
    print("All tests complete")
