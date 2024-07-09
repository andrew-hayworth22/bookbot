def main():
    path = "books/frankenstein.txt"
    print_book_report(path)

def print_book_report(path):
    text = get_book_text(path)
    word_count = get_word_count(text)

    char_counts = get_character_counts(text)
    char_count_list = []
    for char in char_counts:
        if char.isalpha():
            char_count_list.append({
                "char": char,
                "occurrences": char_counts[char]
            })
    char_count_list.sort(reverse=True, key=sort_on_occurrences)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    for char_count in char_count_list:
        print(f"The '{char_count['char']}' character was found {char_count['occurrences']} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(book_text):
    return len(book_text.split())

def get_character_counts(book_text):
    counts = {}

    lowered_text = book_text.lower()
    for char in lowered_text:
        if char not in counts:
            counts[char] = 1 
        else:
            counts[char] += 1

    return counts

def sort_on_occurrences(dict):
    return dict["occurrences"]

main()