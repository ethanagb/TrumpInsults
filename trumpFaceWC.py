import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

insults = open('./trumpInsults.txt','r').read()
trump_mask = np.array(Image.open('trump2.png'))

bannedWords = ['said','new','will','york','many','the','total','never','united','states','failing','totally','news','bad','failed','people','senator',
              'party','one','state','always','absolutely','governor','make','read','anything','always','good','thing','really','job','lost','show','group',
              'nothing','story','television','political','time','cruz','talk','zero','organization', 'guy','even','deal','false','history','looking',
              'reporting','look','country','poll','say','ratings','vote','money','former','president','press','republican','reporter','politician','magazine',
              'much','debate','debates','times','campaign','presidential','fox','clinton','hillary','bush','credibility','candidate','know','columnist','immigration',
              'another','ad','lied','chief','ted','record','newspaper','another','paid','journal','way','trump','got','life',
              'last','dead','street','great','clue','jeb']

for word in bannedWords:
    STOPWORDS.add(word)

wc = WordCloud(background_color="white", max_words=1500, mask=trump_mask, stopwords=STOPWORDS)
wc.generate(insults)
wc.to_file('trumpInsultWC.png')