from typing import List
import collections
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        dict_words = {}
        set_banned = set (banned)
        
        string_to_analyse = paragraph.lower()
        
        for word in re.findall(r"[\w]+", string_to_analyse):
            
            if word not in set_banned:
                if word in dict_words.keys():
                    dict_words[word] +=1
                else:
                    dict_words[word] = 1
        
        word_counter = collections.Counter(dict_words)
        
        return word_counter.most_common(1)[0][0]


# TIME O(words_num + banned_words)
# SPACE O (words_num + banned_words)