import random
import string

with open('book.txt', 'r') as file:
    text = file.read()

text = text.lower()

new_text = ''
for word in text:
    if word in string.punctuation:
        new_text += ' '
    else:
        new_text += word
words = new_text.split()

words_dict = {}
for i in range(len(words) - 1):
    curr_words = words[i]
    following_word = words[i + 1]
    if curr_words not in words_dict:
        words_dict[curr_words] = []
    words_dict[curr_words].append(following_word)

any_word = random.choice(list(words_dict.keys()))
final_text = [any_word]

for _ in range(199):
    next_word_options = words_dict.get(any_word)
    if not next_word_options:
        break
    next_word = random.choice(next_word_options)
    final_text.append(next_word)
    any_word = next_word

print(' '.join(final_text))
