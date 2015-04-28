print('Hello')
anagram=input('What is your name?\n')
anagramcompare='a b c d e f g h i j k l m n o p q r s t u v w x y z'
splitanagram=anagramcompare.split()
mtf=0
if len(anagram)>0:
    for i in range(len(anagram)):
        tf= False
        tf= anagram[i] in splitanagram[:]
        if tf==True:
            mtf = mtf + 1
        #return mtf
if mtf == len(anagram):
            print('Did you know that',anagram,'is a anagram?')
elif i ==len(anagram)-1:
    print('Hello,',anagram)
    