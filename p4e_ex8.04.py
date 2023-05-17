fname = input('Enter the file name: ')
fhand = open(fname)

count = 0

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    count = count + 1
    words = line.split()
    print(words[1])

print('There were', count, 'lines.')

# line = "From zqian@umich.edu Fri Jan  4 16:10:39 2008"

# words = line.split()
# print(words)
# email = words[1]
# piece = email.split('@')
# print(piece[1])

# for line in fhand:
#     line = line.rstrip()
#     wds = line.split()
#     if len(wds) < 3 or wds[0] != 'From':
#         continue
#     print(wds[3])