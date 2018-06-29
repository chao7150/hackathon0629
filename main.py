# -*- coding: utf-8 -*-
from janome.tokenizer import Tokenizer
import random
import os
import pandas as pd


def main():
    text = input("input: ")
    sentences = text.split("。")[:-1]
    if len(sentences) == 0:
        sentences = [text]
    modulated_sentences = []
    for sentence in sentences:
        modulated_sentence = modulate(sentence)
        if modulated_sentence == "":
            continue
        modulated_sentences.append(modulated_sentence)
    
    print("")
    print(("。".join(modulated_sentences) + "。").replace("。。", "。"))


def modulate(sentence):
    template_meibun = pick_meibun()
    t = Tokenizer()
    tokens = t.tokenize(sentence)
    nouns = []
    verbs = []
    for token in tokens:
        word = token.surface
        part = token.part_of_speech.split(",")[0]
        if part == "名詞":
            nouns.append(word)
        if part == "動詞":
            verbs.append(word)
    words = []
    for i, d in template_meibun.iterrows():
        if d[4] == "名詞" and len(nouns) != 0:
            words.append(nouns.pop(0))
        elif d[4] == "動詞" and len(verbs) != 0:
            words.append(verbs.pop(0))
        else:
            words.append(d[3])
    return "".join(words)


def pick_meibun():
    resource = os.path.join("resources", random.choice(os.listdir("resources")))
    sentence_df = pick_sentence(resource)
    return sentence_df


def pick_sentence(resource):
    df = pd.read_csv(resource, header=None)
    sentence_num = random.randint(1, df[1].max())
    sentence_df = df[df[1] == sentence_num][[2, 3, 4]]
    return sentence_df


if __name__ == "__main__":
    main()
