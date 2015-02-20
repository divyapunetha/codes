__author__ = 'divya'
str1 = raw_input()
str2 = raw_input()
list1 = list(str1)
list2 = list(str2)
def is_anagram():
    list1.sort()
    list2.sort()
    if (list1 == list2):
        print "IS ANAGRAM"
    else:
        print "IS NOT ANAGRAM"
is_anagram()
