OUT = 0
IN = 1
def countWords(string):
    state = OUT
    a = 0
    for i in range(len(string)):
        if (string[i] == ' ' or string[i] == '\n' or
            string[i] == '\t'):
            state = OUT
        elif state == OUT:
            state = IN
            a += 1
    return a
 
string ="this is great thanks very much"
print("No. of words : " + str(countWords(string)))