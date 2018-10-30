import sys

def __in_words_2_digits(num):
    '''
    expected num to be < 100
    '''
    l1 = ',one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventee,eighteen,nineteen,twenty'.split(',')

    l2 = ',,twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety'.split(',')

    if num<=20: return l1[num]

    n1 = num//10
    n2 = num%10
    word = l2[n1] + ' ' + l1[n2]
    return word.strip()

def num2words(num):
    if num>999999999:
        print('Number too big. Try less than 100 crores.')
        return

    units = []
    c = 0
    l1 = ',hundred,thousand,lakh,crore'.split(',')
    while num>0:
        div = 10 if c==1 else 100
        word = __in_words_2_digits(num%div)
        if word!='': 
            units.insert(0, word)
            units.insert(1, l1[c])

        num //= div
        c += 1

    return ' '.join(units)

def main():
    num = int(sys.argv[1]) if len(sys.argv)>1 else None

    if num==None:
        print('You must supply a number as commandline argument!')
        exit()

    in_words = num2words(num)
    print(in_words)
    


if __name__=='__main__': main()

