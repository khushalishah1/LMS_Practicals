'''Write a program for computing GCD of 2 numbers with optimal data structures and less time-consuming.'''

def words_to_number(number1):

    '''
        Function converts word to number as string format.

    :param number1: taken string as parameter.

    :return: return the converted string from word to number.
    '''

    if 'zero' in number1:
        number1=number1.replace("zero","0")
    if 'one' in number1:
        number1=number1.replace('one','1')
    if 'two' in number1:
        number1=number1.replace('two','2')
    if 'three' in number1:
        number1=number1.replace('three','3')
    if 'four' in number1:
        number1=number1.replace('four','4')
    if 'five' in number1:
        number1=number1.replace('five','5')
    if 'six' in number1:
        number1=number1.replace('six','6')
    if 'seven' in number1:
        number1=number1.replace('seven','7')
    if 'eight' in number1:
        number1=number1.replace('eight','8')
    if 'nine' in number1:
        number1=number1.replace('nine','9')
    return number1


def number_to_word(number1):

    '''
       function for numbert to word created.

    :param number1: taken string as parameter which have numbers in string format.

    :return: return the converted string from number to word as given output.
    '''

    if '0' in number1:
        number1=number1.replace("0","zero")
    if '1' in number1:
        number1=number1.replace('1','one')
    if '2' in number1:
        number1=number1.replace('2','two')
    if '3' in number1:
        number1=number1.replace('3','three')
    if '4' in number1:
        number1=number1.replace('4','four')
    if '5' in number1:
        number1=number1.replace('5','five')
    if '6' in number1:
        number1=number1.replace('6','six')
    if '7' in number1:
        number1=number1.replace('7','seven')
    if '8' in number1:
        number1=number1.replace('8','eight')
    if '9' in number1:
        number1=number1.replace('9','nine')
    return number1

def gcd(a,b):
    '''
      function for gcd of two number

    :param a: first number from console

    :param b: second number from console

    :return: return the gcd of the two numbers.
    '''
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

''' Take two numbers from user '''

number1=input("enter 1st number ")
number2=input("enter 2nd number ")


'''
    Convert the word_to_number function's return string to an integer.
      
'''
n1=int(words_to_number(number1))
n2=int(words_to_number(number2))

#calling gcd function .
answer=gcd(n1,n2)

#converting int to string and calling number_to_word function.
answer=number_to_word(str(answer))

#printing answer as a list format.
print( "answer = "+answer)






