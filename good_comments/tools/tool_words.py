# -*- coding: utf-8 -*-
import pandas as pd
import re
import jieba

df = pd.read_csv('comment.csv')
content = df['好']

words_list = []

stopwords = []
stay_words = []

word_freq = {}
freq_word = []


# cut sentences and save words_list
def cut(line):
    if type(line) is not float:
        seg_list = jieba.cut(line, cut_all=False)
        line = list(seg_list)
        words_list.extend(line)
    return words_list


# delete stopwords
def delete(text,seg_list):
    l =[]
    file = open(text)
    for line in file:
        line = re.sub(r'\n', '', line)
        l.append(line)
    stopwords = {}.fromkeys(l)

    for word in words_list:
        if word not in stopwords:
            stay_words.append(word)
    return stay_words

# word frequency
def sort(max_number):
    for word in stay_words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    for word, freq in word_freq.items():
        freq_word.append((word, freq))
    freq_word.sort(key=lambda x: x[1], reverse=True)

    for word, freq in freq_word[: max_number]:
        print(word, freq)
    return freq_word

# save
def save(filename):
    file = open(filename,'w',encoding='utf-8')
    for word,freq in freq_word:
        file.write(word+str(freq)+'\n')
    file.close()


# improve stopwords list
def add_words(append_list,text):
    file = open(text,'a+')
    for word in file:
        file.write(word + '\n')
    file.close()


# run
def main():
    print('Sure')
    content.map(cut)
    delete('商品评论停词.txt',words_list)
    sort(0)
    save('路由器分词.txt')


if __name__ == '__main__':
    main()