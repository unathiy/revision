sentence = input("Enter a sentence:")

sentence = sentence.lower()

word_list = []
word = ''

for char in sentence:
    if char != ' ':
        word += char
    else:
        word_list.append(word)
        word = ''

word_list.append(word)

for i in range(len(word_list)):
    if i < len(word_list) - 1:
        print(word_list[i] + ",", end= ' ')
    else:
        print(word_list[i] + ".", end='')
