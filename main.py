from stats import count_words, count_chars, sort_dictionaries
import sys

def get_book_text(path):
    book_content = ""
    with open(path) as f:
        book_content = f.read()
    return book_content



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count -------")
    sorted_dict_list = sort_dictionaries(count_chars(get_book_text(sys.argv[1])))
    for dict in sorted_dict_list:
        if dict["name"].isalpha():
            print(f"{dict["name"]}: {dict["num"]}")

main()