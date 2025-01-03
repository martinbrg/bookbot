def count_words(text):
    words_list = text.split() 
    return len(words_list)

def get_book_text(path):
    with open(path) as file:
        return file.read()

def count_chars(text):
    chars_dict = {}
    # to lower so we don't count duplicates
    lowered_text = text.lower()
    for char in lowered_text:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def sort_on(item):
    # A function that takes a dictionary item and returns the value of the given key
    # This is how the `.sort()` method knows how to sort the list of dictionaries
    return item["num"]

def sort_output(dict):
    output_list = []
    for char, count in dict.items():
        if char.isalpha():
            output_list.append({"char": char, "num": count})


    return output_list

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_chars(text)
    output_list = sort_output(chars_dict)
    sorted_output = output_list.sort(key=sort_on, reverse=True)    

    # printing report
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for item in output_list:
        print(f"The '{item["char"]}' character was found {item["num"]} times")
    print("--- End of report ---")




main()