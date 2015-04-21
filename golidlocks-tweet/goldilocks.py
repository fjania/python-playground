#from http://stackoverflow.com/questions/8982163/how-do-i-tell-python-to-convert-integers-into-words
def numToWords(num,join=True):
    '''words = {} convert an integer number into words'''
    units = ['','one','two','three','four','five','six','seven','eight','nine']
    teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
             'seventeen','eighteen','nineteen']
    tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', \
            'eighty','ninety']
    thousands = ['','thousand','million','billion','trillion','quadrillion', \
                 'quintillion','sextillion','septillion','octillion', \
                 'nonillion','decillion','undecillion','duodecillion', \
                 'tredecillion','quattuordecillion','sexdecillion', \
                 'septendecillion','octodecillion','novemdecillion', \
                 'vigintillion']
    words = []
    if num==0: words.append('zero')
    else:
        numStr = '%d'%num
        numStrLen = len(numStr)
        groups = (numStrLen+2)/3
        numStr = numStr.zfill(groups*3)
        for i in range(0,groups*3,3):
            h,t,u = int(numStr[i]),int(numStr[i+1]),int(numStr[i+2])
            g = groups-(i/3+1)
            if h>=1:
                words.append(units[h])
                words.append('hundred')
            if t>1:
                words.append(tens[t])
                if u>=1: words.append(units[u])
            elif t==1:
                if u>=1: words.append(teens[u])
                else: words.append(tens[t])
            else:
                if u>=1: words.append(units[u])
            if (g>=1) and ((h+t+u)>0): words.append(thousands[g]+',')
    if join: return ' '.join(words)
    return words

def vowel_count(sentence):
    vc = 0
    for v in ['a','e','i','o','u']:
        vc += sentence.lower().count(v)

    return vc

base = "This is a 'goldilocks tweet'. It's got {} characters, {} of which are spaces, and {} of which are vowels.".format('{}', '{}', '{}')

c = len(base)
s = base.count(' ');
v = vowel_count(base)


for c_count in range(c, c+100):
    for s_count in range(s, s+10):
        for v_count in range(v, v+20):
            a = base.format(
                numToWords(c_count),
                numToWords(s_count),
                numToWords(v_count),
            )

            v_real = vowel_count(a)
            v_test = v_count - v_real

            s_real = a.count(' ')
            s_test = s_count - s_real

            c_real = len(a)
            c_test = c_count - c_real

            if (
                c_test == 0 and
                v_test == 0 and
                s_test == 0
                ):
                print "{} {} {} {}".format(c_real, s_real, v_real, a)
