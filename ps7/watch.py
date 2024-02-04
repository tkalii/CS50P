import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        url_pattern = re.search(r"(https?:\/\/(www\.)?youtube\.com\/embed\/)([\w]+)", s)
        if url_pattern := url_pattern.groups():
            return "https://youtu.be/" + url_pattern[2]
    else:
        return False

if __name__ == "__main__":
    main()