sentence = input("Enter the sentence: ")
words_list = sentence.split()
longest = 0
for word in words_list:
    if len(word) > longest:
        longest = len(word)
        longest_word = word
print("The longest word is %s" % longest_word)
word_reversed = sentence[::-1]
print("Sentence of reversed words : %s " % word_reversed)
no_of_words = len(words_list)
middle_word = []
if no_of_words%2==0:
    middle_word.append(words_list[(no_of_words//2)-1])
    middle_word.append(words_list[no_of_words//2])
else:
    middle_word.append(words_list[no_of_words//2])
print("Middle word is : %s" % middle_word)