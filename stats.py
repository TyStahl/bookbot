def get_word_count(booktext):
    w = booktext.split()
    word_count = len(w)
    return word_count

def get_char_count(booktext):
    text_length = len(booktext)
    text_lower = booktext.lower()
    char_count = {}
    for i in range(0, text_length-1):
        if text_lower[i] not in char_count:
            char_count[text_lower[i]] = 1
        else:
            char_count[text_lower[i]] += 1 
    return char_count

def get_dict_report(dictionary):
    report = []
    for key in dictionary:
        if key.isalpha():
            report.append({"char":key, "num": dictionary[key]})
    def sort_on(dictionary):
        return dictionary["num"]
    report.sort(reverse=True, key=sort_on)
    return report

