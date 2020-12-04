import csv
#import bertmoticon
import demoji
from textblob import TextBlob
import re
import unicodedata
from unidecode import unidecode
import textstat

data = [("day", "time", "tweet", "polarity", "subjectivity","retweets")]
analysed_data = []

def format_line(line):
    line = demoji.replace(line)
    line = re.sub(r"(@\S*)", "@", line)
    line = re.sub(r"http://\S*", "url", line)
    return line

with open('realdonaldtrump.csv', encoding='Latin-1') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    for row in readCSV:
        tweet = format_line(row[2])
        #print(row)
        testimony = TextBlob(tweet)
        #grade_level = textstat.coleman_liau_index(tweet)
        time_and_date = row[3]
        day = time_and_date[0:10]
        time = time_and_date[11:16]
        retweets = row[4]
        individual = (day,time,tweet,testimony.sentiment.polarity, testimony.sentiment.subjectivity,retweets)
        data.append(individual)


with open('final_f.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
