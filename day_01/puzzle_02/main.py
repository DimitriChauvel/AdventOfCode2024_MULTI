"""Day 01 Puzzle 02"""

def main():
    """Main function"""
    with open("input.txt", encoding="utf-8") as file:
        splited = file.read().split("\n")
        left = [int(line.split("   ")[0]) for line in splited]
        right = [int(line.split("   ")[1]) for line in splited]

        print(sum(value * right.count(value) for value in left))


if __name__ == "__main__":
    main()
