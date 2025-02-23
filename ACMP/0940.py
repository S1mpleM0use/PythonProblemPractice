number, word = map(str, input().split())
for i in range(len(word)+1):
    if i+1 == int(number):
        new_word = list(word)
        new_word.pop(i)


print(''.join(new_word))