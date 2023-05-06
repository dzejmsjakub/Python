fname = input('Enter the file name: ')

if fname == 'na na boo boo':
    print(fname.upper(), "- You have been punk'd!")
    quit()

try:
    fhand = open(fname)
except:
    print('File cannot be found.')
    quit()

count = 0
sum = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        colpos = line.find(':')
        value = float(line[colpos+1:])
        sum = sum + value
        count = count + 1

print('Average spam confidence: ', round(sum/count, 12))