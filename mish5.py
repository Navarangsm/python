words = ['apple',"banana",'apple','orange',"banana","apple"]
unique = list(set(words))
word_count = dict(map(lambda word: (word,words.count(word)),unique))
print("output:",word_count)

#from collections import Counter
#words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
#word_counts = dict(Counter(words))
#print("output:",word_counts)