def getchar() -> str:
    inp = input()
    if inp == "":
        inp = " "
    return inp[0]


def putchar(char: str):
    print(end=char, flush=True)
