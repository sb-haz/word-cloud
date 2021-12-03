# Imports 
from wordcloud import WordCloud, STOPWORDS
import sys, os
os.chdir(sys.path[0])

# Read text
text = open('text.txt', mode='r', encoding='utf-8').read()
stopwords = STOPWORDS

# WordCloud
wc = WordCloud(
    background_color = 'white',
    stopwords = stopwords,
    height = 1000,
    width = 1000
)

# Generate
wc.generate(text)
 
# Store to file
wc.to_file('output.png')