filename = open("twain.txt")
 
words_count = {}

for lines in filename:
    stripped_line_list = lines.rstrip()
    lower_line_list = stripped_line_list.upper()
    split_line_list = lower_line_list.split(" ")

#for each word in line_list make each word a key and give a value of 0


    for word in split_line_list:
        if word in words_count:
            words_count[word] = words_count[word] + 1
        else:
            words_count[word]= 1

for word,count in words_count.items():
    print word, count





