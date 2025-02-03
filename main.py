def sort_on(alpha_chars):
    return alpha_chars["num"]

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    alpha_chars = []
    for char, count in chars_dict.items():
        alpha = {"name": char, "num": count}
        alpha_chars.append(alpha)

    alpha_chars.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    for char_dict in alpha_chars:
        print(f"The '{char_dict['name']}' character was found {char_dict['num']} times")

    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()