# Imports 
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image # load image
import numpy as np # get colour of image

# Content-related
text = open('batman.txt', 'r', encoding='utf-8').read()
stopwords = STOPWORDS

# Appearance-related
custom_mask = np.array(Image.open('batman.png'))

wc = WordCloud(
    mask = custom_mask,
    background_color = 'white',
    stopwords = stopwords,
    height = 1000,
    width = 1000
)
# Generate
wc.generate(text)

# Store to file
wc.to_file('batman_output.png')