def extract_lexemes(token_array):
    symbols = ['{', '}', '(', ')','\n']
    comparison_operators = ['>', '<', '==', '>=', '<=']
    operators = ['+', '-','=']
    int_support = ['8', '16', '32', '64', '128']
    if_else = ['if', 'else']
    declare_variable = ['var']
    data_types = ['int']
    variable = ['x','y']

    lexemes = []
    lexeme = ''
    amount_token = len(token_array)
    i = 0
    
    while i < amount_token:
        token = token_array[i]

        if token.isalpha():
            lexeme = token
            if lexeme in declare_variable:
                lexemes.append('declare_variable')
            elif lexeme in variable:
                lexemes.append('variable')
            elif lexeme in data_types:
                lexemes.append('data_types')
            elif lexeme in if_else:
                lexemes.append('if_else')
            else:
                lexeme = ''

        elif token.isdigit():
            lexeme = token
            if lexeme in int_support:
                lexemes.append('int_support')
            else:
                lexeme = ''

        elif token in comparison_operators:
            lexemes.append('comparison_operator')
            lexeme = ''

        elif token in operators:
            lexemes.append('operator')
            lexeme = ''

        elif token in symbols:
            if (lexeme and (lexeme != 'else') and (lexeme != 'y') and (lexeme != 'int32') and (lexeme != 'int64')):
                lexemes.append(lexeme)
                lexeme = ''

            if token != '\n':
                lexemes.append(token)

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
    token = code.split()
    print('==================================\nThis is the lexemes')
    print('==================================\n')
    lexemes = extract_lexemes(token)
    for lexeme in lexemes:
       print(lexeme)
    
if __name__ == '__main__':
    main()