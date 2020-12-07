filee = open('text.txt', 'r')

res = {}
lines = filee.readlines()
word = []
word_list=[]

def add_word(word):
    word = word.strip().lower()

    if word in res:
        res[word] += 1
    else:
        res[word] = 1


list(map(lambda x: word_list.extend(x.strip().split()), lines))
list(map(add_word, word_list))

print(res)


   
