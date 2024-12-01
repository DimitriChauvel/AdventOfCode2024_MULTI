"""Day 01 Puzzle 01"""

def main():
    """Main function"""
    with open("input.txt", encoding="utf-8") as file:
        splited = file.read().split("\n")
        left = list(sorted([int(line.split("   ")[0]) for line in splited]))
        right = list(sorted([int(line.split("   ")[1]) for line in splited]))

        print(sum(abs(left[i] - right[i]) for i in range(len(left))))


if __name__ == "__main__":
    main()
