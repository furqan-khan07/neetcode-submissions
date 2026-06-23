from typing import List

def read_integers() -> List[int]:
    lis = []
    red = input()


    lisput = red.split(",")

    for inte in lisput:
        lis.append(int(inte))

    return lis

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
