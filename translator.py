from deep_translator import GoogleTranslator

#source -> your language
#target -> Target language for example if it is spanish then use -> es

translator = GoogleTranslator(
    source='auto',
    target='es'
)

text = "_put your text here_"

print(translator.translate(text))

