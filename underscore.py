import string

import pyperclip

OK_CHARS = string.ascii_letters + string.digits

def underscore(x: str, /):
    x = x.lower()
    words = []
    chars = []
    def push():
        if chars:
            words.append(''.join(chars))
            chars.clear()
    for char in x:
        if char in OK_CHARS:
            chars.append(char)
        else:
            push()
    push()
    return '_'.join(words)

def test():
    def testOne(x):
        print(x)
        print(underscore(x))
    testOne('Oh my bass.')
    testOne('Lily\'s pond')
    testOne('ha _~! ha')

def main():
    x = pyperclip.paste()
    print('In clipboard:', x)
    y = underscore(x)
    print('Result:')
    pyperclip.copy(y)
    print(y)
    print('Copied to clipboard.')

if __name__ == '__main__':
    # test()
    main()
