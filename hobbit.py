#!/usr/bin/env python3
"""
Multiple functions for already written text(hobbit.txt).

@date 2022-10-08
@author Igor Simunovic <igorsimunovic2@gmail.com>
"""
import argparse
import re


def hobbitAppend():
    with open('hobbit.txt', 'r') as contents:
        save = contents.read()
    with open('hobbit.txt', 'w') as contents:
        contents.write("I really love this tale by J.R.R.Tolkein!\n")
    with open('hobbit.txt', 'a') as contents:
        contents.write(save)
    txt = open("hobbit.txt", "a")
    txt.write("I Really love this tale by J.R.R.Tolkein!\n")
    print("Added new row in the beggining and to the end of hobbit.txt")
    txt.close()
    # In this instance i left the two functions together, even tho the functions can be devided and called separatly.
    # function simply adds sentence at start and end of hobbit.txt


def hobbitRead():
    txt = open("hobbit.txt", "r")
    text = txt.read()
    print(text)
    txt.close()
    # the function simply prints out the hobbit.txt


def hobbitCheckBut():
    txt = open("hobbit.txt", "r")
    text = txt.read()
    x = re.findall('but', text)
    if len(x) > 1:
        print("There are {} sentences with word but in hobbit.txt.".format(len(x)))
    elif len(x) == 1:
        print("There is {} sentence with but in hobbit.txt".format(len(x)))
    else:
        ("There are {} sentences with word but in hobbit.txt.".format(len(x)))
    # the function checks for all but words in hobbit.txt and prints out the number of them.
    # sa else sam stavio zbog mogucnosti nule ,a da ne bih sirio gore sa or u if statmentu.

    txt.close()


def hobbitCheckIt():
    txt = open("hobbit.txt", "r")
    text = txt.read().split(".")
    sentence = list(text)
    sentenceWithIt = []
    for i in sentence:
        k = re.findall('^It+', str(i))
        if k:
            sentenceWithIt.append(i)
        else:
            z = re.findall('\n^It', str(i))
            if z:
                sentenceWithIt.append(i)
    if len(sentenceWithIt) > 1:
        print("There are {} sentances that start with It in hobbit.txt".format(len(sentenceWithIt)))
    elif len(sentenceWithIt) == 1:
        print("There is {} sentance that start with It in hobbit.txt".format(len(sentenceWithIt)))
    else:
        print("There are {} sentances that start with It in hobbit.txt".format(len(sentenceWithIt)))
    txt.close()
    # this function finds and prints the number of sentences that start with "It"
    # sa else sam stavio zbog mogucnosti nule ,a da ne bih sirio gore sa or u if statmentu.


def hobbitCheckUs():
    txt = open("hobbit.txt", "r")
    text = txt.read().split(".")
    sentence = list(text)
    sentencesWithUs = []
    for i in sentence:
        k = re.findall("us$", str(i))
        if k:
            sentencesWithUs.append(i)
        else:
            z = re.findall("us/n$", str(i))
            if z:
                sentencesWithUs.append(i)
    print("hobbit.txt has {} us at the end of sentence.".format(len(sentencesWithUs)))
    # this function finds and prints the number of sentences that end with "us".


def hobbitWordCounter():
    txt = open("hobbit.txt", "r")
    text = txt.read()
    x = re.findall(r'\w', text)
    print("There are {} words in hobbit.txt".format(len(x)))
    # this function simply counts the number of words in hobbit.txt


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-a','--append',help="appends line of text in hobbit.txt at the beggining and end",action='store_true')
#     parser.add_argument('-r','--read',help = "reads the hobbit.txt and prints it out",action='store_true')
#     parser.add_argument('-b','--but',help = "checks for word but in hobbit.txt and prints out the number",action='store_true')
#     parser.add_argument('-i','--it',help = "checks for word it in hobbit.txt and prints out the number",action='store_true')
#     parser.add_argument('-u','--us',help = "checks for word us in hobbit.txt and prints out the number",action='store_true')
#     parser.add_argument('-c','--count',help= "counts the number of words in hobbit.txt and prints out the number",action='store_true')
#     parser.add_argument('-e','--everything',help='calls all functions from above',action='store_true')
#     args = parser.parse_args()

#     append = args.append
#     read = args.read
#     but = args.but
#     it = args.it
#     us = args.us
#     count = args.count
#     everything = args.everything

#     if args.append:
#         hobbitAppend()
#     if args.read:
#         hobbitRead()
#     if args.but:
#         hobbitCheckBut()
#     if args.it:
#         hobbitCheckIt()
#     if args.us:
#         hobbitCheckUs()
#     if args.count:
#         hobbitWordCounter()
#     if args.everything:
#         hobbitAppend()
#         hobbitRead()
#         hobbitCheckBut()
#         hobbitCheckIt()
#         hobbitCheckUs()
#         hobbitWordCounter()


# hobbitAppend()
# hobbitRead()
# hobbitCheckBut()
# hobbitCheckIt()
# hobbitCheckUs()
# hobbitWordCounter()