#!/usr/bin/python

import scanner
import ply.yacc as yacc
import AST

tokens = scanner.tokens

precedence = (
    ("nonassoc", "IFX"),
    ("nonassoc", "ELSE"),

    ("right", '=', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
    ("left", 'EQUALS', 'NOTEQUALS', '>', '<', 'LESEQ', 'MOREEQ'),
    ("left", '+', '-', 'DOTADD', 'DOTSUB'),
    ("left", '*', '/', 'DOTMUL', 'DOTDIV'),
    ("right", 'ONES', 'ZEROS', 'EYE'),
    ("left", "'"),
    ("right", ":"),
    ("left", "NEG"),
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_instructions(p):
    """
    instructions : instruction
              | instructions instruction
    """
    if len(p) == 2:
        p[0] = AST.Instructions([p[1]])
    else:
        instr = p[1]
        p[1].instructions.append(p[2])
        p[0] = instr


def p_instruction(p):
    """
    instruction : expression ';'
                  | empty_instr
                  | break_stmt
                  | continue_stmt
                  | return_stmt
                  | print_stmt
                  | if_stmt
                  | while_stmt
                  | for_stmt
                  | '{' instructions '}'
    """
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[1]


def p_empty_instr(p):
    """
    empty_instr : ';'
                  | '{' '}'
    """
    p[0] = AST.Instructions([])


def p_expression(p):
    """
    expression :   binary_expr
                 | compare_expr
                 | negation
                 | assignment
                 | mcreate
                 | sub_matrix
                 | transposition
                 | '(' expression ')'
                 | pvector
                 | int
                 | float
                 | string
                 | variable
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_submatrix(p):
    """
    sub_matrix : expression pvector
    """
    p[0] = AST.Submatrix(p[1], p[2])


def p_parenthesised_vector(p):
    """
    pvector : '[' ']'
             | '[' vector ']'
    """
    if len(p) == 4:
        p[0] = AST.Vector(p[2])
    else:
        p[0] = AST.Vector([])


def p_vector(p):
    """
    vector : expression
             | vector ',' expression
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1]
        p[0].append(p[3])


def p_int(p):
    """
    int :   INTNUM
    """
    p[0] = AST.IntNum(p[1])


def p_float(p):
    """
    float : FLOATNUM
    """
    p[0] = AST.FloatNum(p[1])


def p_string(p):
    """
    string : STRING
    """
    p[0] = AST.String(p[1])


def p_variable(p):
    """
    variable : ID
    """
    p[0] = AST.Variable(p[1])


def p_binary_expr(p):
    """
    binary_expr : expression '+' expression
                 | expression '-' expression
                 | expression '*' expression
                 | expression '/' expression
                 | expression DOTADD expression
                 | expression DOTSUB expression
                 | expression DOTMUL expression
                 | expression DOTDIV expression
    """
    p[0] = AST.BinExpr(p[2], p[1], p[3])


def p_compare_expr(p):
    """
    compare_expr :  expression '>' expression
                  | expression '<' expression
                  | expression LESEQ expression
                  | expression MOREEQ expression
                  | expression NOTEQUALS expression
                  | expression EQUALS expression
    """
    p[0] = AST.BinExpr(p[2], p[1], p[3])


def p_negation(p):
    """
    negation : '-' expression %prec NEG
    """
    p[0] = AST.UnaryExpr(p[1], p[2])


def p_assignment(p):
    """
    assignment : variable '=' expression
                 | variable ADDASSIGN expression
                 | variable SUBASSIGN expression
                 | variable MULASSIGN expression
                 | variable DIVASSIGN expression
                 | sub_matrix '=' expression
                 | sub_matrix ADDASSIGN expression
                 | sub_matrix SUBASSIGN expression
                 | sub_matrix MULASSIGN expression
                 | sub_matrix DIVASSIGN expression
    """
    p[0] = AST.Assignment(p[1], p[2], p[3])


def p_transposition(p):
    """
    transposition : expression "'"
    """
    p[0] = AST.UnaryExpr(p[2], p[1])


def p_mcreate(p):
    """
    mcreate :  EYE '(' expression ')'
             | ZEROS '(' expression ')'
             | ONES '(' expression ')'
    """
    p[0] = AST.UnaryExpr(p[1].upper(), p[3])


def p_break_stmt(p):
    """
    break_stmt : BREAK ';'
    """
    p[0] = AST.BreakStatement()


def p_continue_stmt(p):
    """
    continue_stmt : CONTINUE ';'
    """
    p[0] = AST.ContinueStatement()


def p_return_stmt(p):
    """
    return_stmt : RETURN expression ';'
    """
    p[0] = AST.ReturnStatement(p[2])


def p_print_stmt(p):
    """
    print_stmt : PRINT vector ';'
    """
    p[0] = AST.PrintStatement(p[2])


def p_range(p):
    """
    range : expression ':' expression
    """
    p[0] = AST.RangeStatement(p[1], p[3])


def p_if_stmt(p):
    """
    if_stmt : IF '(' expression ')' instruction %prec IFX
            | IF '(' expression ')' instruction ELSE instruction
    """
    if len(p) == 6:
        p[0] = AST.IfStatement(p[3], p[5])
    else:
        p[0] = AST.IfStatement(p[3], p[5], p[7])


def p_while_stmt(p):
    """
    while_stmt : WHILE '(' expression ')' instruction
    """
    p[0] = AST.WhileLoop(p[3], p[5])


def p_for_stmt(p):
    """
    for_stmt : FOR variable '=' range instruction
    """
    p[0] = AST.ForLoop(p[2], p[4], p[5])


parser = yacc.yacc()
