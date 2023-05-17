fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    print('File cannot be found.')
    quit()

words = []
unique_words = []

for line in fhand:
    word = line.split()
    words.extend(word)

for word in words:
   if word not in unique_words:
       unique_words.append(word) 

unique_words.sort()
print(unique_words)