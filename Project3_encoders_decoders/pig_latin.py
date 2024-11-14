#User input word in pig latin
word = input("Input your word in pig latin")

#separate first and second part of word
l = word.split("-")
first = l[0]

#Take the ay off the second part
second = l[1]
ay = second.split("ay")
second = ay[0]

#Print word in english
print(second+first)
