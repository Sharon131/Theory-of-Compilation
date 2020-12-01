#!/usr/bin/python

import scanner
import ply.yacc as yacc

tokens = scanner.tokens

precedence = (
    ("nonassoc", "IFX"),
    ("nonassoc", "ELSE"),

    # ("right", "SUBMATRIX"),
    ("right", '=', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
    ("left", 'EQUALS', 'NOTEQUALS', '>', '<', 'LESEQ', 'MOREEQ'),
    ("left", '+', '-', 'DOTADD', 'DOTSUB'),
    ("left", '*', '/', 'DOTMUL', 'DOTDIV'),
    # ("right", 'ONES', 'ZEROS', 'EYE'),
    ("left", "'"),
    ("right", ":"),
    ("left", "NEG"),
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """
    program : instruction
              | program instruction
    """


def p_instruction(p):
    """
    instruction : expression ';'
                  | ';'
                  | if_stmt
                  | while_stmt
                  | for_stmt
                  | BREAK ';'
                  | CONTINUE ';'
                  | RETURN expression ';'
                  | print_stmt
                  | '{' instructions '}'
                  | '{' '}'
    """


def p_instructions(p):
    """
    instructions : instructions instruction
                   | instruction
    """


def p_expression(p):
    """
    expression : expression '+' expression
                 | expression '-' expression
                 | expression '*' expression
                 | expression '/' expression
                 | '-' expression %prec NEG
                 | expression DOTADD expression
                 | expression DOTSUB expression
                 | expression DOTMUL expression
                 | expression DOTDIV expression
                 | expression '>' expression
                 | expression '<' expression
                 | expression LESEQ expression
                 | expression MOREEQ expression
                 | expression NOTEQUALS expression
                 | expression EQUALS expression
                 | ID '=' expression
                 | ID ADDASSIGN expression
                 | ID SUBASSIGN expression
                 | ID MULASSIGN expression
                 | ID DIVASSIGN expression
                 | sub_matrix '=' expression
                 | sub_matrix ADDASSIGN expression
                 | sub_matrix SUBASSIGN expression
                 | sub_matrix MULASSIGN expression
                 | sub_matrix DIVASSIGN expression
                 | sub_matrix
                 | EYE '(' expression ')'
                 | ZEROS '(' expression ')'
                 | ONES '(' expression ')'
                 | expression "'"
                 | '(' expression ')'
                 | '[' ']'
                 | '[' vector ']'
                 | FLOATNUM
                 | INTNUM
                 | ID
                 | STRING
    sub_matrix : expression '[' vector ']'
                | expression '[' range ']'
    vector : expression
             | vector ',' expression
    """


def p_if_stmt(p):
    """
    if_stmt : IF '(' expression ')' instruction %prec IFX
            | IF '(' expression ')' instruction ELSE instruction
    """


def p_while_stmt(p):
    """
    while_stmt : WHILE '(' expression ')' instruction
    """


def p_for_stmt(p):
    """
    for_stmt : FOR ID '=' range instruction
    range : expression ':' expression
    """


def p_print_stmt(p):
    """
    print_stmt : PRINT vector ';'
    """


parser = yacc.yacc()
