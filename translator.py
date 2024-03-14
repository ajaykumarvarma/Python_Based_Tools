from deep_translator import GoogleTranslator

#source -> your language
#target -> Target language for example if spanish then use -> es

translator = GoogleTranslator(
    source='auto',
    target='es'
)

text = "_put your text here_"

print(translator.translate(text))


#----------------------------------

# from textblob import TextBlob

# text = "Hello, world!"
# blob = TextBlob(text)
# translation = blob.translate(to='es')
# print(translation)

#----------------------------------

# from pytranslate import translate

# text = "Hello, world!"
# translation = translate(text, target_lang='es')
# print(translation)

#----------------------------------