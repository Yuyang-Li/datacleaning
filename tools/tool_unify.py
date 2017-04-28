# -*- coding: utf-8 -*-    # import system default encoding
import pandas as pd
import re

# change the type of file

df1 = pd.read_csv('1238332.csv')
df2 = pd.read_csv('2811500.csv')
df3 = pd.read_csv('3153016.csv')
comment = pd.concat([df1, df2, df3])

# no missing data
comment['content'].fillna(0)
comment = comment[comment != 0]


# remove punctuation
def remove_punc(line):
    punctuation = '!,;:?"\'！，。？；：“”().'
    l = re.sub(r'[{}]+'.format(punctuation), '', line)
    return l

def remove_num(line):
    t = re.sub(r'/d','',line)
    return t


# format unified
comment['content'] = comment['content'].map(remove_punc,remove_num)

# remove duplicate value
comment = comment['content'].drop_duplicates()

# save
comment.to_csv('comment.csv',encoding='utf-8')

