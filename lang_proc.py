import string
import re

def removeUnsuitableStringsFromList(l: list, stop_words: list) -> (list, list):
  new_tokens = []; unwanted_tokens = []
  for s in l:
    if s.isnumeric() or s in string.punctuation: unwanted_tokens.append(s); continue # check if is numeric or punctuation (_#. ...)
    if re.search(r'[~=]', s): unwanted_tokens.append(s); continue # search for strange occurenes
    if re.search(r'[\d]+[a-z]+', s): unwanted_tokens.append(s); continue # remove the uuid-like strings
    m = re.search(r'^.*?([\w]+).*?$', s) # remove points from around
    s = m.group(1)
    if s in stop_words: unwanted_tokens.append(s); continue # check if it's in stop words
    new_tokens.append(s)
  return new_tokens, unwanted_tokens