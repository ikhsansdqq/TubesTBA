def extract_lexemes(token_array):
    symbols = ['{', '}','\n']
    comparison_operators = ['>', '<', '==', '>=', '<=']
    operators = ['+', '-','=']
    int_support = [8, 16, 32, 64, 128]
    if_else = ['if', 'else']
    declare_variable = ['var']
    data_types = ['int']
    variable = ['x','y']

    lexemes = []
    i = 0
    i, lexemes = var_check(i,lexemes,token_array,declare_variable,variable,data_types,int_support)
    lexemes = if_else_check(i,lexemes,variable,if_else,comparison_operators,symbols,operators,token_array)
    return lexemes
    
def var_check(i,lexemes,token_array,declare_variable,variable,data_types,int_support):
    lexeme = ''
    lexeme = token_array[i]
    if lexeme in declare_variable:
        lexemes.append('declare_variable')
        i+=1
        lexeme = token_array[i]
        if lexeme in variable:
            lexemes.append('variable')
            i+=1
            lexeme = token_array[i]
            if lexeme in data_types:
                lexemes.append('data_types')
                i+=1
                lexeme = token_array[i]
                if lexeme == '=':
                    lexemes.append('=')
                    i+=1
                    lexeme = token_array[i]
                    if int(lexeme) in int_support:
                        lexemes.append('int_support')
                        i+=1
                        if i < 9:
                            i,lexemes = var_check(i,lexemes,token_array,declare_variable,variable,data_types,int_support)
                        else:
                            return i,lexemes
                    else:
                        raise ValueError("Invalid lexeme: {}".format(lexeme))
                else:
                    raise ValueError("Invalid lexeme: {}".format(lexeme))
            else:
                raise ValueError("Invalid lexeme: {}".format(lexeme))
        else:
            raise ValueError("Invalid lexeme: {}".format(lexeme))
    else:
        raise ValueError("Invalid lexeme: {}".format(lexeme))
    return i,lexemes

def if_else_check(i,lexemes,variable,if_else,comparison_operators,symbols,operators,token_array):
    lexeme = ''
    lexeme = token_array[i]
    if lexeme in if_else:
        lexemes.append('if_else')
        i+=1
        lexeme = token_array[i]
        if lexeme in variable:
            lexemes.append('variable')
            i+=1
            lexeme = token_array[i]
            if lexeme in comparison_operators:
                lexemes.append('comparison_operator')
                i+=1
                lexeme = token_array[i]
                if lexeme in variable:
                    lexemes.append('variable')
                    i+=1
                    lexeme = token_array[i]
                    if lexeme in symbols[0]:
                        lexemes.append('symbols')
                        i = action_check(i,lexemes,variable,operators,token_array)
                        if i < len(token_array):
                            i+=1
                            lexeme = token_array[i]
                            if lexeme in symbols[1]:
                                i+=1
                                lexeme = token_array[i]
                                if lexeme in if_else:
                                    lexemes.append('if_else')
                                    i+=1
                                    lexeme = token_array[i]
                                    if lexeme in symbols[0]:
                                        lexemes.append('symbols')
                                        i = action_check(i,lexemes,variable,operators,token_array)
                                        i+=1
                                        lexeme = token_array[i]
                                        if lexeme in symbols[1]:
                                            lexemes.append('symbols')
                                        else:
                                            raise ValueError("Invalid lexeme: {}".format(lexeme))
                                    else:
                                        raise ValueError("Invalid lexeme: {}".format(lexeme))
                                else:
                                    raise ValueError("Invalid lexeme: {}".format(lexeme))   
                            else:
                                raise ValueError("Invalid lexeme: {}".format(lexeme))
                        else:
                            raise ValueError("Invalid lexeme: {}".format(lexeme)) 
                    else:
                        raise ValueError("Invalid lexeme: {}".format(lexeme)) 
                else:
                    raise ValueError("Invalid lexeme: {}".format(lexeme))
            else:
                raise ValueError("Invalid lexeme: {}".format(lexeme))
        else:
            raise ValueError("Invalid lexeme: {}".format(lexeme))                                
    else:                       
        raise ValueError("Invalid lexeme: {}".format(lexeme))
    return lexemes
    

def action_check(i,lexemes,variable,operators,token_array):
    lexeme = ''
    i+=1
    lexeme = token_array[i]
    if lexeme in variable:
        lexemes.append('variable')
        i+=1
        lexeme = token_array[i]
        if lexeme == '=':
            lexemes.append('=')
            i+=1
            lexeme = token_array[i]
            if lexeme in variable:
                lexemes.append('variable')
                i+=1
                lexeme = token_array[i]
                if lexeme in operators:
                    lexemes.append('operators')
                    i+=1
                    lexeme = token_array[i]
                    if lexeme in variable:
                        lexemes.append('variable')
                    else:
                        raise ValueError("Invalid lexeme: {}".format(lexeme))
                else:
                    raise ValueError("Invalid lexeme: {}".format(lexeme))
            else:
                raise ValueError("Invalid lexeme: {}".format(lexeme))
        else:
            raise ValueError("Invalid lexeme: {}".format(lexeme))
    return i
        


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
    """
    Change inside the "token_input to change the input
    """

    token_input = ''' 
var x int = 32
var y int = 128

if x > y {
 	x = x - y
} else {
	x = x + y
}
    '''
    print(grammar)

    print('This is the code', token_input)
    
    token = token_input.split()
    print("==================================")
    print('Parser result :')
    for tokens  in token:
        print(tokens)
    print("\nParser length :",len(token))
    print('\n==================================\nLexical Analyzer Result: \n')
    lexemes = extract_lexemes(token)
    for lexeme in lexemes:
        print(lexeme)
    
if __name__ == '__main__':
    main()