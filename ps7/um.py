import re
import sys

def main():
    print(count(input("Text: ")))

    
def count(s):
    total = len(re.findall(r"\b\W*um\W*", s))
    return total

if __name__ == "__main__":
    main()