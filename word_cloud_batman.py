# Imports 
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image # load image
import matplotlib.pyplot as plt # display wordcloud
import numpy as np # get colour of image

# Content-related
text = open('batman.txt', 'r', encoding='utf-8').read()

# Appearance-related
wc = WordCloud(
    background_color = 'white',
    
)
# Generate
wc.generate(text)

# Display
plt.imshow(wc, interpolation = 'bilinear')
plt.axis('off')
plt.show()