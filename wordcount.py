# put your code here.
def count_words(file):
    with open(file) as words:
        word_count = {}
        for line in words:
            line = line.rstrip()
            words = line.split(" ")
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
        for word, cnt in word_count.items():
            print(f"{word} {cnt}")     

print("test.txt output:")
count_words('test.txt')
#print("\ntwain.txt output:")
#count_words('twain.txt')