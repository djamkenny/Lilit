def main():
    sentence = input("express your emotion: ")
    print(convert(sentence))

def convert(sentence):
    sentence = sentence.replace(":(","🙁")
    sentence = sentence.replace(":)", "🙂")
    return sentence
main()
