
''' Given an array of strings strs, group the anagrams together.'''

# groupanagrams function created.
def groupanagrams(lst):
    '''
        function  group the  anagram words.

        :param
        lst: input from user.

        :return
        values of dictionary as a list type.

    '''
    anagram_dict={}   #empty dictionary created.

    for word in lst:
        sorted_word="".join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)  #append value in dictionary if key is present in dictionary.
        else:
            anagram_dict[sorted_word]=[word]   #append value in dictionary if key is not present in dictionary.

    return list(anagram_dict.values())

if  __name__=="__main__":
    try:
        string=eval(input("enter array of string: "))  #take input from console.
        if 1<=len(string)<=104:
            for s in string:
                if 0<=len(s)<=100:
                    if s.islower()==False and s!="":
                        raise Exception("Input should be in lower case")  #if word in not lower case then error generate.
                else:
                    raise Exception("Word length increase")  #exception for one string element  in array
        else:
            raise Exception("array of strings length increase") #exception for full array of strings.

        print(groupanagrams(string))


    except Exception as e:
       print("Error: {}".format(str(e)))
       '''
            print the exception error when invalid input is given.
       '''
