def determine_color(s):
    col = ord(s[0]) - ord('a') + 1
    row = int(s[1])

    if (col + row) % 2 == 0:
        return "Black"
    else:
        return "White"

def main():
    import sys
    input = sys.stdin.read
    s = input().strip()

    result = determine_color(s)
    print(result)

if __name__ == "__main__":
    main()