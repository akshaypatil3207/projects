#written by Akshay Patil
# pig latin word is nothing but taking first con sonets upto arrival of a vowel and putting it to the last followed by "ay"
#eg pig == igpay
#if word starts with vowel then simply add "yay" after the word
#eg apple == appleyay

#first take a sentence from user and convert it into pig latin

 #taking sentance from user
string=input("Enter the sentence to be translated :- ")
words=string.split()


#take individual word and if first letter is vowel then append "yay" and save it in same list
#else find index of first vowel, take all the following letters till length of word, then append 0 to index letters and then append "ay" and save
for i in words:
    if i[0].lower() in "aeiou":
        words[words.index("{}".format(i))]=i+"yay"
    else:
        for j in i:
            if j.lower() in "aeiou":
                vow_index=i.index("{}".format(j))
                translay=i[vow_index:len(i)]
                translay+=i[0:vow_index]+"ay"
                words[words.index("{}".format(i))]=translay
                break
#join the new words from list as a sentence
# method one

#out=""
#for i in words:
#    out=out+" {}".format(i)

#method two
# this can be simply done by join keyword
out=" ".join(words)

print("The translated sentance is :- \" {} .\" ".format(out))



