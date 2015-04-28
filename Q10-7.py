print('Hello')
anagram=input('What is your name?\n')
anagramcompare='a b c d e f g h i j k l m n o p q r s t u v w x y z'
splitanagram=anagramcompare.split()
print(splitanagram)
for i in range(len('anagram')-1):
    mtf=0.0
    tf= anagram[i] in splitanagram
    print(i,anagram[i])
    print(tf,mtf)
    if tf==True:
        mtf = mtf + 1.0
        if mtf == len('anagram')-1:
            print('Did you know that',anagram,'is a anagram?')
        elif i ==3:
            print('Hello,',anagram)