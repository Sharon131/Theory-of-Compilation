import ply.lex as lex

# List of reserved words

reserved = {
    'if':       'IF',
    'else':     'ELSE',
    'for':      'FOR',
    'while':    'WHILE',
    'break':    'BREAK',
    'continue': 'CONTINUE',
    'return':   'RETURN',
    'eye':      'EYE',
    'zeros':    'ZEROS',
    'ones':     'ONES',
    'print':    'PRINT'
}

# List of token names.
tokens = [
    'ID',
    'INTNUM',
    'FLOATNUM',
    'STRING',
    'COMMENT',
    'SUBASSIGN',
    'ADDASSIGN',
    'MULASSIGN',
    'DIVASSIGN',
    'LESEQ',
    'MOREEQ',
    'NOTEQUALS',
    'EQUALS',
    'DOTADD',
    'DOTSUB',
    'DOTMUL',
    'DOTDIV'
] + list(reserved.values())

# A regular expression rule with some action code
t_SUBASSIGN = r'-='
t_ADDASSIGN = r'\+='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'/='
t_LESEQ = r'<='
t_MOREEQ = r'>='
t_NOTEQUALS = r'!='
t_EQUALS = r'=='
t_DOTADD = r'\.\+'
t_DOTSUB = r'\.-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\./'


def t_ID(t):
    r'[A-Za-z_]+[A-Za-z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_FLOATNUM(t):
    r'(\d*\.\d+)|(\d+\.\d*)(E\d+)?'
    t.value = float(t.value)
    return t


def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'\".*\"'
    t.value = t.value[1:-1]
    return t


def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Literals
literals = "=+-*/:'{}()[]<>,;"

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s' in line %d" % (t.value[0], t.lexer.lineno))
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


# Compute column.
#     text is the input text string
#     token is a token instance
def find_column(text, token):
    line_start = text.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1
