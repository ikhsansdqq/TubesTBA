def extract_lexemes(code):
    symbols = ['{', '}', '(', ')','\n']
    comparison_operators = ['>', '<', '==', '>=', '<=']
    operators = ['+', '-']
    int_support = ['8', '16', '32', '64', '128']
    if_else = ['if', 'else']
    declare_variable = ['var']
    data_types = ['int']
    variable = ['x','y']

    lexemes = []
    lexeme = ''
    i = 0

    while i < len(code):
        char = code[i]

        if char.isalpha():
            lexeme += char
            if i+1 < len(code) and not code[i+1].isalpha():
                if lexeme in declare_variable:
                    lexemes.append('variable')
                elif lexeme in data_types:
                    lexemes.append('data_types')
                elif lexeme in if_else:
                    lexemes.append('if_else')
                elif lexeme in variable:
                    lexemes.append('variable')
                else:
                    lexeme = ''

        elif char.isdigit():
            lexeme += char
            if i+1 < len(code) and not code[i+1].isdigit():
                if lexeme.startswith('int') and lexeme[3:] in int_support:
                    lexemes.append('int_support')
                else:
                    lexeme = ''

        elif char in comparison_operators:
            lexemes.append('comparison_operator')
            lexeme = ''

        elif char in operators:
            lexemes.append('operator')
            lexeme = ''

        elif char in symbols:
            if (lexeme and (lexeme != 'else') and (lexeme != 'y') and (lexeme != 'int32') and (lexeme != 'int64')):
                lexemes.append(lexeme)
                lexeme = ''

            if char != '\n':
                lexemes.append(char)

        i += 1

    return lexemes


def main():
    grammar = '''
Grammar:

<statement> ::= var <variable> int = <int_support>
<variable> ::= x | y
<if-else_block> := if <condition> { <action> } else { <action> }
<condition> ::= <variable> <comparison_operator> <variable>
<action> ::= <variable> = <variable> <operator> <variable>
<operator> ::= + | - 
<comparison_operator> ::= > | < | == | >= | <=
<int_support> ::= 8 | 16 | 32 | 64 | 128

    '''
    code = ''' 
var x int = 32
var y int = 16

if x > y {
 	x = x - y
} else {
	x = x + y
}
    '''
    print(grammar)

    print('This is the code', code)
    lexemes = extract_lexemes(code)
    for lexeme in lexemes:
        print(lexeme)
    
if __name__ == '__main__':
    main()