import sys

def main():
    for s in sys.argv:
        for c in s:
            print(c)
        print(s)


if __name__== '__main__':
    main()