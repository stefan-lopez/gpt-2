import csv

text_writer = open("parsed_trump_tweets.txt", "a", encoding = 'utf-8-sig')

with open('trump_tweets.csv', 'r', newline = '', encoding = 'utf-8') as file:
    reader = csv.reader(file, delimiter = ',')
    next(reader)
    prev_row = []
    for row in reader:
        entry = row[0] + '<|endoftext|>'
        try:
            text_writer.write(entry)
        except:
            pass
  
text_writer.close()