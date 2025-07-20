
def get_num_words(content):
    return len(content.split())

def get_char_count(content):
    char_count = {}
    word_list = content.split()
    for i in word_list:
        for j in i.lower():
            if j not in char_count:
                char_count[j] = 1
            else:
                char_count[j] += 1
    return char_count

def get_sort_list(content):
    sort_char = []
    for i,j in content.items():
        sort_char.append({"name": i, "num": j})
    
    def sort_on(items):
        return items["num"]
    sort_char.sort(reverse=True, key=sort_on)
    return sort_char