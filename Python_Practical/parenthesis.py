''' Generate parenthesis from given number '''

def generateparentheses(open,close,n,answer,s):
    '''
       This function generate the parentheses as a list.

      :param open: this parameter for open parentheses.

      :param close: this parameter for close parentheses.

      :param n: input given by user.

      :param answer: final list for printing output.

      :param s: temorary string for storing every value during iteration.

      :return: none
      '''


    if(open==n and close==n):
        answer.append(s)
        return

    if open<n :
        generateparentheses(open+1,close,n,answer,s+"(")

    if close<open :
        generateparentheses(open,close+1,n,answer,s+")")



if  __name__=="__main__":
    try:
        n = int(input("enter a number "))  # Take input from user.
        if not 1<=n<=8:
            raise Exception("Input should be in valid range.") #Raise exception if range is not valid.
        print(f'number is {n}.')

        # declare empty list named answer which store our program's final output..
        answer = []

        # calling the function generateperentheses
        generateparentheses(0, 0, n, answer, "")

        # print all elements which is in answer list=>which shows us the given output.
        print(answer)


    except Exception as e:
        print("Error: {}".format(str(e)))
        '''
             print the exception error when invalid input is given.
        '''