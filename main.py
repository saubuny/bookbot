from io import TextIOWrapper


def main():
    with open("books/frankenstein.txt") as book:
        report(book)


def word_count(book: str) -> int:
    return len(book.split())


def word_freq(book: str) -> dict[str, int]:
    freq = {}
    for ch in book:
        ch = ch.lower()
        if ch.isalpha():
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1
    return freq


def report(book: TextIOWrapper):
    contents = book.read()
    print(f"-- Report of {book.name} ---")
    print(f"{word_count(contents)} words found\n")

    freq_list = []
    freq_dict = word_freq(contents)
    for ch in freq_dict:
        freq_list.append({"char": ch, "freq": freq_dict[ch]})

    freq_list.sort(reverse=True, key=sort_on)
    for entry in freq_list:
        print(f"The {entry["char"]} character was found {entry["freq"]} times")

    print("-- End report ---")

def sort_on(dict: dict):
    return dict["freq"]

main()
