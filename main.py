from textblob import TextBlob

def Convert(string):
    return list(string.split())

str1 = input("Enter your word : ")
words = Convert(str1)
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
    
print("Wrong words : ", words)
print("Corrected Words are : ")
for i in corrected_words:
    print(i.correct(), end= " ")