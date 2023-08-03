#!/usr/bin/env python3

class MyString:
    def __init__(self, word=None):
        self._word = word

    def get_string(self):
        return self._word

    def set_string(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
            return
        self._word = value

    word = property(get_string, set_string)
    value = word  # Alias for word property

    def is_sentence(self):
        return self._word.endswith(".") if self._word else False

    def is_question(self):
        return self._word.endswith("?") if self._word else False

    def is_exclamation(self):
        return self._word.endswith("!") if self._word else False

    def count_sentences(self):
     if not self._word:
        return 0
   
     sentence_string = self._word.replace('!', '.').replace('?', '.')
  
     sentences = [s for s in sentence_string.split('.') if s.strip()]
     return len(sentences)






            
          

              
            
        

