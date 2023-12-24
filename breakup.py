sentence = input("Enter a sentence:") #to input a sentence 

sentence = sentence.lower() #converts the sentence to lower case

word_list = [] #create an empty list
word = ''

for char in sentence:
    if char != ' ':
        word += char
    else:
        word_list.append(word)
        word = ''

word_list.append(word) #appends the last word

#to print the list separated by commas
for i in range(len(word_list)):
    if i < len(word_list) - 1:
        print(word_list[i] + ",", end= ' ') #places comma and space
    else:
        print(word_list[i] + ".", end='') #if last word, puts full stop
