def get_book_text(rel_file_path):
    with open(rel_file_path) as f:
        contents = f.read()
    return contents

def main():
    import sys
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    from stats import count_words
    from stats import count_characters
    from stats import sorted_count
    print(f"Analyzing book found at {sys.argv[1]}...")
    contents = get_book_text(sys.argv[1])
    num = count_words(contents)
    character_dictionary = count_characters(contents)
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    dict_list = sorted_count(character_dictionary)
    for char in dict_list:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")


main()