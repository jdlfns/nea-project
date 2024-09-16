from deep_translator import GoogleTranslator

# FUNCTION mainTranslate()
# originalLanguage = sourceLang()
# targetLanguage = targetLang()
# // Retrieve the text that the user inputs, then translate it into the target language 
# text = “Hello World!”
# translated = DeepLTranslator(originalLanguage, targetLanguage).translate(text)
# RETURN translated


text = 'happy coding'
translated = GoogleTranslator(source='auto', target='de').translate(text=text)
print(translated)