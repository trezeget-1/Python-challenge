import os

paragraph_file = os.path.join("raw_data","paragraph_1.txt")

with open(paragraph_file,"r") as text:
    lines = text.read()

# Sentence count

sentences=[]

for i in range(len(lines)):
    sentences=lines.split(".")

sentence_count=(len(sentences)-1)

# Average Sentence Length

number_of_words_on_each_sentence=[]

for i in range(len(sentences)):
    sentences[i]=sentences[i].split(" ")    
    number_of_words_on_each_sentence.append(len(sentences[i]))

sum=0

for i in number_of_words_on_each_sentence:
    sum+=i

average_sentence_length=sum/sentence_count
average_sentence_length=round(average_sentence_length,1)

# Approximate Word Count:

words=[]
characters_count=0

for i in range(len(sentences)):
    for x in range(len(sentences[i])):
        words.append(sentences[i][x])

for i in range(len(words)):
    for x in range(len(words[i])):
        characters_count+=len(words[i][x])

total_number_of_words=(len(words))

# Average Letter Count:

average_letter_count=characters_count/total_number_of_words
average_letter_count=round(average_letter_count,1)

results=(f"""
```
Paragraph Analysis
-----------------
Approximate Word Count: {total_number_of_words}
Approximate Sentence Count: {sentence_count}
Average Letter Count: {average_letter_count}
Average Sentence Length: {average_sentence_length}
```
""")

print(results)