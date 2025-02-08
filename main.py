def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        # Word count
        print(word_count(file_contents))
        character_count_report(character_count(file_contents))


def word_count(book):
    count = 0
    for word in book.split():
        count += 1
    return count


def character_count(string):
    letters = {}
    for char in string.lower():
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters


def character_count_report(file):
    count = file
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in letters:
        if letter in count:
            print(f"The '{letter}' character was found {count[letter]} times.")

main()
