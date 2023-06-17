def extract_lexemes(code):
    symbols = ['{', '}', '(', ')', '[', ']', '.', '"', '*', '\n', ':', ',']
    other_symbols = ['\\', '/*', '*/']
    keywords = ['func', 'main', 'var', 'int32', 'if', 'else']
    KEYWORDS = symbols + other_symbols + keywords

    lexemes = []
    lexeme = ''

    for char in code:
        if char == '*':
            if lexeme and lexeme[-1] == '/':
                lexeme += '*'
            else:
                lexeme += char
        elif char == '/':
            if lexeme and lexeme[-1] != '*':
                lexeme += char
        else:
            if char != ' ':
                lexeme += char

        if char in KEYWORDS or lexeme in KEYWORDS:
            if lexeme:
                lexemes.append(lexeme.replace('\n', '<newline>'))
                lexeme = ''

    return lexemes


def main():
    code = '''
    func main() {
        var x int32 = 5
        var y int32 = 10

        if x > y {
            fmt.Println("x is greater than y")
        } else {
            fmt.Println("x is less than or equal to y")
        }
    }
    '''

    lexemes = extract_lexemes(code)
    for lexeme in lexemes:
        print(lexeme)


if __name__ == '__main__':
    main()
text_input = input("Please input the teks!\n")
text_input = text_input.replace(' ', '')

print("The parsing")
for i in text_input:
    print(i)
