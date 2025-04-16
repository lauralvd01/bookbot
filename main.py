import sys
from stats import get_num_words, get_characters_count, sort_characters_count

def get_book_text(filepath) :
    with open(filepath) as f :
        return f.read()

def main() :
    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else :
        filepath = sys.argv[1]
        text = get_book_text(filepath)
        num_words = get_num_words(text)
        characters_count = get_characters_count(text)
        sorted_list = sort_characters_count(characters_count)
        
        print('''============ BOOKBOT ============
    Analyzing book found at ''' + str(filepath) + '''...
    ----------- Word Count ----------
    Found ''' + str(num_words) + ''' total words
    --------- Character Count -------''')
        for char, count in sorted_list :
            print(f"{char}: {count}")
        print('''============= END ===============''')
    
if __name__ == "__main__" :
    main()