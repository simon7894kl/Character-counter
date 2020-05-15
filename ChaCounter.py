from collections import Counter

long_str = '''The new patients were an 18-year-old female student who returned from Britain on Friday, 
and a 61-year-old man whose granddaughter and domestic helper was infected previously, according to Dr Chuang Shuk-kwan, 
head of the Centre for Health Protection’s communicable disease branch.'''

res = Counter(long_str)

print("Count of all characters in the sentence :\n "
      + str(res))

