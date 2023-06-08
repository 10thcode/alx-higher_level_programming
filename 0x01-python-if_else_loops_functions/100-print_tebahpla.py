#!/usr/bin/python3

def main():
    print_tebahpla()


def print_tebahpla():
    for i in range(90, 64, -1):
        if i % 2 == 0:
            i += 32
        print("{:c}".format(i), end="")


if __name__ == "__main__":
    main()
