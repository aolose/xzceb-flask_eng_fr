from deep_translator import MyMemoryTranslator


def englishToFrench(english_text):
    french_text = MyMemoryTranslator(source='en-US', target='fr-FR').translate(english_text)
    return french_text


def frenchToEnglish(french_text):
    english_text = MyMemoryTranslator(source='fr-FR', target='en-US').translate(french_text)
    return english_text
