import ftfy
import re
import string

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('portuguese'))

def remove_html(text: str) -> str:
  text = re.sub(r'&[a-zA-Z0-9#]+;', ' ', text)
  return re.sub('<[^<]+?>', ' ', text)

def remove_multiple_spaces(text: str) -> str:
  result = re.sub('\\s{2,}', ' ', text)
  return result

def remove_wrong_diacritics(text: str):
  # Remove acentos isolados e outros caracteres que não fazem sentido
  # Mantém letras, números, espaços e pontuações importantes
  return re.sub(r'[^\w\s,.!?;:/()\[\]%-]', '', text)

def remove_punctuation(text: str):
  translator = str.maketrans('', '', string.punctuation)
  return text.translate(translator)

def compose(*functions):
  def inner(arg):
    for f in functions:
      arg = f(arg)
    return arg
  return inner

def clean_text(text: str) -> str:
  cleaning = compose(
    ftfy.fix_text,
    remove_html,
    remove_wrong_diacritics,
    remove_multiple_spaces,
    str.strip
  )
  return cleaning(text)

def remove_stopwords(text):
  words = text.split()
  
  filtered_words = [
    word for word in words if word.lower() not in stop_words and word not in string.punctuation
  ]
  return ' '.join(filtered_words)