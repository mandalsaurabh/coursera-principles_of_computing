"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"

# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but with no duplicates.

    This function can be iterative.
    """
    _set = []
    for _item in list1:
        if _item not in _set:
            _set.append(_item)
    return _set

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    _set = []
    for _item in list1:
        if _item in list2:
            _set.append(_item)
    return _set

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that are in either list1 and list2.

    This function can be iterative.
    """
    if list1 == []:
        return list2
    if list2 == []:
        return list1
    if list1 == [] and list2 == []:
        return []
    
    _set = list1 + list2
    _copy = _set[:]
    _low = 0
    _high = len(list1)
    #print "list",_set
    for _index in range(_low,len(_set)):
        #print _index,_set
        #print _low,_high
        if _low >= len(list1):
            _set[_index] = _copy[_high]
            _high+=1
        elif _high >= len(_set):
            _set[_index] = _copy[_low]
            _low+=1
        elif _copy[_low] <= _copy[_high]:
            _set[_index] = _copy[_low]
            _low+=1
        elif _copy[_low] > _copy[_high]:
            _set[_index] = _copy[_high]
            _high+=1
    return _set
        
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) < 2:
        return list1
    _subleft = list1[:len(list1)/2]
    _subright = list1[len(list1)/2:]
    _left = merge_sort(_subleft)
    _right = merge_sort(_subright)
    return merge(_left,_right)
   


# Function to generate all strings for the word wrangler game
def insert_pos(_str,_char):
    """
    insert character into all position in origin string
    @param _str : The origin string
    @param _char: a character
    @return a list of string
    """
    return [_str[:_index]+_char+_str[_index:] for _index in range(len(_str)+1)]

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word in any order.
    @param word:
    
    Returns a list of all strings that can be formed from the letters in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return ['']
    _item_pop = word[-1]
    _next = gen_all_strings(word[:-1])
    #print _item_pop,_next
    _ans = []
    for _item in _next[:]:
        _ans.extend(insert_pos(_item,_item_pop))
    _ans.extend(_next)
    return _ans


# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return urllib2.urlopen(codeskulptor.file2url(filename))

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
#run()
