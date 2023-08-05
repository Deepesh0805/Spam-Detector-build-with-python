import pandas as pd
#----------------------------------------PROBABILITY CALCULATIONS----------------------------------------------------------------------------
def total(d1):
    """PROBABILITY CALCULATION """
    count =0
    for a in d1:
        count+=d1[a]

    return count

def like(c1,c2):
    """PROBABILITY CALCULATION """

    return(c1/(c1+c2))

def prob(li,c):
    """PROBABILITY CALCULATION """
    for i in li:
        li[i]=li[i]/c
    return li

def blackbox(li):
    """PROBABILITY CALCULATION """
    for i in li:
        li[i]+=1
    return li
#----------------------------------------PROBABILITY CALCULATIONS----------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------
def creating_dict(l):
    """Function which creates a dictionary, by count of each words"""
    d1=dict()
    for i in l:
        for asd in i:
            for j in asd.split():
                k=j.lower()
                if k not in d1:
                    d1[k]=1
                else:
                    d1[k]=d1[k]+1
    return d1
#--------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------
def remove_punctuations(string_value):
    """Function that removes all punctuations in given list"""
    punctuations = '''!()-[]};{:'",<|>./?@#$%^&*_~'''
    string_edited = ""

    for letter in string_value:
        if letter not in punctuations:
            string_edited = string_edited + letter
    temp_list=string_edited.split() 
    string_edited = " ".join(temp_list)
    return string_edited
#--------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------
def predict(): 
    """Function which accepts Email-text from the user and predicts if the Email-text is spam or ham"""
    user_string = input("Enter your E-mail text : ")
    user_string=remove_punctuations(user_string)
    L=user_string.split(" ")
    p1=normal_prob
    p2=spam_prob
    for i in L:
        if i in n_event:
            p1=p1*n_event[i]
        else:
            p1=p1

        if i in s_event:
            p2=p2*s_event[i]
        else:
            p2=p2
    if p1>p2 :
        print("Ham mail")
        print(p1)
    else:
        print("Spam mail")
#-------------------------------------------------------------------------------------------------------------------- 

#--------------------------------------------------------------------------------------------------------------------
"""The .py file and csv file should be in same folder"""
data = pd.read_csv("file1.csv")
text_list = data.values.tolist()
all = []
normal = []
spam = []
for i in text_list:
    all.append([remove_punctuations(i[0])])
    if(i[1] == "ham"):
        normal.append([remove_punctuations(i[0])])
    else:
        spam.append([remove_punctuations(i[0])])

n_event=creating_dict(normal)
s_event=creating_dict(spam)
t_event=creating_dict(all)
for i in t_event:
    if i not in n_event:
        n_event[i]=0
    if i not in s_event:
        s_event[i]=0
n_event=blackbox(n_event)
s_event=blackbox(s_event)
count1=total(n_event)
count2=total(s_event)
n_event=prob(n_event,count1)
s_event=prob(s_event,count2)
normal_prob=like(count1,count2)
spam_prob=like(count2,count1)

predict()
