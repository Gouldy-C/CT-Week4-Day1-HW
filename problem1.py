#6 kyu
#In this simple Kata your task is to create a function that turns a string into a Mexican Wave.
#You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 



def wave(people):  #time O(n^2)  #space O(n)
    res_list = []   #time O(1)  #space O(1)
    for i, l in enumerate(people):   #time O(2n)  #space O(0)
        if l != " ":   #time O(1)  #space O(0)
            p_list  = list(people)   #time O(n)  #space O(n)
            p_list[i] = p_list[i].upper()    #time O(1)  #space O(0)
            res_list.append(''.join(p_list))    #time O(n)  #space O(n)
    return res_list     #time O(1)  #space O(1)