from deep_translator import MyMemoryTranslator


def englishToFrench(english_text):
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text


def frenchToEnglish(french_text):
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
