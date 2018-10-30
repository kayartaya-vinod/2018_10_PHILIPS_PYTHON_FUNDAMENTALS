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
    return __in_words_2_digits(num)

def main():
    num = int(sys.argv[1]) if len(sys.argv)>1 else None

    if num==None:
        print('You must supply a number as commandline argument!')
        exit()

    in_words = num2words(num)
    print(in_words)
    


if __name__=='__main__': main()

