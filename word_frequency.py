def text_word(text):
    words = text.split()
    
    frequency = {}

    for word in words:

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    sorted_frequency = dict(sorted(frequency.items()))
    
    return sorted_frequency

text = input("Type your text: ")
print("Word List:", sorted(text_word(text).keys()))
print("\nBag of Words:")
for word, count in text_word(text).items():
    print(word, "-", count)
