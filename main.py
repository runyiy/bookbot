from stats import get_num_words, get_char_count,get_sort_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        book_content = get_book_text(filepath)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(book_content)} total words")
        print("--------- Character Count -------")
        char_dict = get_char_count(book_content)
        sort_char = get_sort_list(char_dict)
        for i in sort_char:
            if i["name"].isalpha():
                print(f"{i["name"]}: {i["num"]}")

if __name__=='__main__':
    main()