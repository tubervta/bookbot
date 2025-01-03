import string

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()

    alphDict = {}
    for letters in string.ascii_lowercase:
        alphDict[letters] = 0
        count = 0
        for char in file_contents:
            if char.lower() == letters:
                count = count + 1
        alphDict[letters] = count
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")
    alphDict = dict(sorted(alphDict.items(), reverse=True, key=lambda item: item[1]))
    for key in alphDict:
        print(f"The '{key}' character was found {alphDict[key]} times")
    print("--- End report ---")

main()