def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count(text):
    words = text.split()
    return len(words)

text = main()
word_count = count(text)
print(word_count)