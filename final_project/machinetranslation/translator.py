# 1.Use the MyMemoryTranslator from the deep_translator python package. (1)
from deep_translator import MyMemoryTranslator

# 2.Create an instance of the MyMemoryTranslator Service in your Python code. (1)
translatorService = MyMemoryTranslator()


def create_translator(target: str, source: str):
    def translator(text: str):
        translatorService.source = source
        translatorService.target = target
        return translatorService.translate(text)

    return translator


# 3.Create a function that translates English to French. (2)
englishToFrench = create_translator('fr', 'en')

# 4.Create a function that translates French to English. (2)
frenchToEnglish = create_translator('en', 'Fr')