# Imports 
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image # load image
import numpy as np # get colour of image

# Content-related
text = open('batman.txt', 'r', encoding='utf-8').read()
stopwords = STOPWORDS

# Mask
custom_mask = np.array(Image.open('batman.png'))

# WordCloud attributes
wc = WordCloud(
    font_path = 'SFProDisplay-Light.ttf',
    #margin = 10,
    mask = custom_mask,
    background_color = 'black',
    #background_color = None,
    #mode = 'RGBA',
    stopwords = stopwords,
    height = 1000,
    width = 1000,
    include_numbers = False, # include numbers
    #color_func=lambda *args, **kwargs: (255,255,255) # text colour
)
# Generate
wc.generate(text)

# Use colour of mask image
## image_colours = ImageColorGenerator(custom_mask)
## wc.recolor(color_func = image_colours)

# Store to file
wc.to_file('batman_output.png')