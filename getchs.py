def getchs(n: int = 1) -> str:
    from sys import stdin
    from termios import TCSADRAIN, tcgetattr, tcsetattr
    from tty import setraw

    fd = stdin.fileno()
    old = tcgetattr(fd)
    try:
        setraw(fd)
        return stdin.read(n)
    finally:
        tcsetattr(fd, TCSADRAIN, old)


if __name__ == "__main__":
    print("\n\x1b[1;33mPress any key...\x1b[0m")
    ch = getchs(3)
    for i in ch:
        print(repr(i), ord(i))
