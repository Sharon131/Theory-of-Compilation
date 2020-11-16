
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocIFXnonassocELSErightSUBMATRIXright=ADDASSIGNSUBASSIGNMULASSIGNDIVASSIGNleftEQUALSNOTEQUALS><LESEQMOREEQleft+-DOTADDDOTSUBleft*/DOTMULDOTDIVrightONESZEROSEYEleft\'right:leftNEGADDASSIGN BREAK COMMENT CONTINUE DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQUALS EYE FLOATNUM FOR ID IF INTNUM LESEQ MOREEQ MULASSIGN NOTEQUALS ONES PRINT RETURN STRING SUBASSIGN WHILE ZEROS\n    program : instruction\n              | program instruction\n    \n    instruction : expression \';\'\n                  | \';\'\n                  | if_stmt\n                  | while_stmt\n                  | for_stmt\n                  | BREAK \';\'\n                  | CONTINUE \';\'\n                  | RETURN expression \';\'\n                  | print_stmt\n                  | \'{\' instructions \'}\'\n                  | \'{\' \'}\'\n    \n    instructions : instructions instruction\n                   | instruction\n    \n    expression : expression \'+\' expression\n                 | expression \'-\' expression\n                 | expression \'*\' expression\n                 | expression \'/\' expression\n                 | \'-\' expression %prec NEG\n                 | expression DOTADD expression\n                 | expression DOTSUB expression\n                 | expression DOTMUL expression\n                 | expression DOTDIV expression\n                 | expression \'>\' expression\n                 | expression \'<\' expression\n                 | expression LESEQ expression\n                 | expression MOREEQ expression\n                 | expression NOTEQUALS expression\n                 | expression EQUALS expression\n                 | ID \'=\' expression\n                 | ID ADDASSIGN expression\n                 | ID SUBASSIGN expression\n                 | ID MULASSIGN expression\n                 | ID DIVASSIGN expression\n                 | sub_matrix \'=\' expression\n                 | sub_matrix ADDASSIGN expression\n                 | sub_matrix SUBASSIGN expression\n                 | sub_matrix MULASSIGN expression\n                 | sub_matrix DIVASSIGN expression\n                 | sub_matrix %prec SUBMATRIX\n                 | EYE \'(\' expression \')\'\n                 | ZEROS \'(\' expression \')\'\n                 | ONES \'(\' expression \')\'\n                 | expression "\'"\n                 | \'(\' expression \')\'\n                 | \'[\' \']\'\n                 | \'[\' vector \']\'\n                 | FLOATNUM\n                 | INTNUM\n                 | ID\n                 | STRING\n    sub_matrix : expression \'[\' vector \']\'\n                | expression \'[\' range \']\'\n    vector : expression\n             | vector \',\' expression\n    \n    if_stmt : IF \'(\' expression \')\' instruction %prec IFX\n            | IF \'(\' expression \')\' instruction ELSE instruction\n    \n    while_stmt : WHILE \'(\' expression \')\' instruction\n    \n    for_stmt : FOR ID \'=\' range instruction\n    range : expression \':\' expression\n    \n    print_stmt : PRINT vector \';\'\n    '
    
_lr_action_items = {';':([0,1,2,3,4,5,6,7,8,9,11,12,14,15,21,22,23,28,29,44,46,47,48,49,50,51,52,67,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,92,93,94,95,96,97,98,99,100,101,102,103,105,108,113,115,116,117,118,119,120,121,122,123,125,126,127,128,129,130,],[4,4,-1,29,-4,-5,-6,-7,46,47,-11,4,-51,-41,-49,-50,-52,-2,-3,-45,-8,-9,91,4,-13,-15,-20,-47,-55,113,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-10,-12,-14,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,-62,-53,-54,-42,-43,-44,-56,4,4,4,-61,-57,-59,-60,4,-58,]),'BREAK':([0,1,2,4,5,6,7,11,12,14,15,21,22,23,28,29,44,46,47,49,50,51,52,67,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,92,93,94,95,96,97,98,99,100,101,102,103,105,108,113,115,116,117,118,119,121,122,123,125,126,127,128,129,130,],[8,8,-1,-4,-5,-6,-7,-11,8,-51,-41,-49,-50,-52,-2,-3,-45,-8,-9,8,-13,-15,-20,-47,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-10,-12,-14,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,-62,-53,-54,-42,-43,-44,8,8,8,-61,-57,-59,-60,8,-58,]),'CONTINUE':([0,1,2,4,5,6,7,11,12,14,15,21,22,23,28,29,44,46,47,49,50,51,52,67,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,92,93,94,95,96,97,98,99,100,101,102,103,105,108,113,115,116,117,118,119,121,122,123,125,126,127,128,129,130,],[9,9,-1,-4,-5,-6,-7,-11,9,-51,-41,-49,-50,-52,-2,-3,-45,-8,-9,9,-13,-15,-20,-47,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-10,-12,-14,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,-62,-53,-54,-42,-43,-44,9,9,9,-61,-57,-59,-60,9,-58,]),'RETURN':([0,1,2,4,5,6,7,11,12,14,15,21,22,23,28,29,44,46,47,49,50,51,52,67,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,92,93,94,95,96,97,98,99,100,101,102,103,105,108,113,115,116,117,118,119,121,122,123,125,126,127,128,129,130,],[10,10,-1,-4,-5,-6,-7,-11,10,-51,-41,-49,-50,-52,-2,-3,-45,-8,-9,10,-13,-15,-20,-47,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-10,-12,-14,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,-62,-53,-54,-42,-43,-44,10,10,10,-61,-57,-59,-60,10,-58,]),'{':([0,1,2,4,5,6,7,11,12,14,15,21,22,23,28,29,44,46,47,49,50,51,52,67,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,92,93,94,95,96,97,98,99,100,101,102,103,105,108,113,115,116,117,118,119,121,122,123,125,126,127,128,129,130,],[12,12,-1,-4,-5,-6,-7,-11,12,-51,-41,-49,-50,-52,-2,-3,-45,-8,-9,12,-13,-15,-20,-47,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-10,-12,-14,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,-62,-53,-54,-42,-43,-44,12,12,12,-61,-57,-59,-60,12,-58,]),'-':([0,1,2,3,4,5,6,7,10,11,12,13,14,15,17,20,21,22,23,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,],[13,13,-1,31,-4,-5,-6,-7,13,-11,13,13,-51,-41,13,13,-49,-50,-52,13,-2,-3,13,13,13,13,13,13,13,13,13,13,13,13,13,13,-45,13,-8,-9,31,13,-13,-15,-20,13,13,13,13,13,13,13,13,13,13,13,31,13,13,-47,31,13,13,-16,-17,-18,-19,-21,-22,-23,-24,31,31,31,31,31,31,31,-10,-12,-14,31,31,31,31,31,31,31,31,31,31,31,-46,31,31,-48,13,31,31,13,-62,13,-53,-54,-42,-43,-44,31,13,13,13,31,-61,-57,-59,-60,13,-58,]),'ID':([0,1,2,4,5,6,7,10,11,12,13,14,15,17,20,21,22,23,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,70,71,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,92,93,94,95,96,97,98,99,100,101,102,103,105,108,109,112,113,114,115,116,117,118,119,121,122,123,125,126,127,128,129,130,],[14,14,-1,-4,-5,-6,-7,14,-11,14,14,-51,-41,14,14,-49,-50,-52,72,14,-2,-3,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-45,14,-8,-9,14,-13,-15,-20,14,14,14,14,14,14,14,14,14,14,14,14,14,-47,14,14,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-10,-12,-14,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,14,14,-62,14,-53,-54,-42,-43,-44,14,14,14,-61,-57,-59,-60,14,-58,]),'EYE':([0,1,2,4,5,6,7,10,11,12,13,14,15,17,20,21,22,23,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,70,71,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,92,93,94,95,96,97,98,99,100,101,102,103,105,108,109,112,113,114,115,116,117,118,119,121,122,123,125,126,127,128,129,130,],[16,16,-1,-4,-5,-6,-7,16,-11,16,16,-51,-41,16,16,-49,-50,-52,16,-2,-3,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-45,16,-8,-9,16,-13,-15,-20,16,16,16,16,16,16,16,16,16,16,16,16,16,-47,16,16,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-10,-12,-14,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,16,16,-62,16,-53,-54,-42,-43,-44,16,16,16,-61,-57,-59,-60,16,-58,]),'ZEROS':([0,1,2,4,5,6,7,10,11,12,13,14,15,17,20,21,22,23,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,70,71,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,92,93,94,95,96,97,98,99,100,101,102,103,105,108,109,112,113,114,115,116,117,118,119,121,122,123,125,126,127,128,129,130,],[18,18,-1,-4,-5,-6,-7,18,-11,18,18,-51,-41,18,18,-49,-50,-52,18,-2,-3,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-45,18,-8,-9,18,-13,-15,-20,18,18,18,18,18,18,18,18,18,18,18,18,18,-47,18,18,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-10,-12,-14,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,18,18,-62,18,-53,-54,-42,-43,-44,18,18,18,-61,-57,-59,-60,18,-58,]),'ONES':([0,1,2,4,5,6,7,10,11,12,13,14,15,17,20,21,22,23,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,70,71,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,92,93,94,95,96,97,98,99,100,101,102,103,105,108,109,112,113,114,115,116,117,118,119,121,122,123,125,126,127,128,129,130,],[19,19,-1,-4,-5,-6,-7,19,-11,19,19,-51,-41,19,19,-49,-50,-52,19,-2,-3,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-45,19,-8,-9,19,-13,-15,-20,19,19,19,19,19,19,19,19,19,19,19,19,19,-47,19,19,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-10,-12,-14,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,19,19,-62,19,-53,-54,-42,-43,-44,19,19,19,-61,-57,-59,-60,19,-58,]),'(':([0,1,2,4,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,70,71,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,92,93,94,95,96,97,98,99,100,101,102,103,105,108,109,112,113,114,115,116,117,118,119,121,122,123,125,126,127,128,129,130,],[17,17,-1,-4,-5,-6,-7,17,-11,17,17,-51,-41,63,17,65,66,17,-49,-50,-52,70,71,17,-2,-3,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-45,17,-8,-9,17,-13,-15,-20,17,17,17,17,17,17,17,17,17,17,17,17,17,-47,17,17,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-10,-12,-14,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,17,17,-62,17,-53,-54,-42,-43,-44,17,17,17,-61,-57,-59,-60,17,-58,]),'[':([0,1,2,3,4,5,6,7,10,11,12,13,14,15,17,20,21,22,23,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,],[20,20,-1,45,-4,-5,-6,-7,20,-11,20,20,-51,-41,20,20,-49,-50,-52,20,-2,-3,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-45,20,-8,-9,45,20,-13,-15,-20,20,20,20,20,20,20,20,20,20,20,20,45,20,20,-47,45,20,20,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,45,-10,-12,-14,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,45,-46,45,45,-48,20,45,45,20,-62,20,-53,-54,-42,-43,-44,45,20,20,20,45,-61,-57,-59,-60,20,-58,]),'FLOATNUM':([0,1,2,4,5,6,7,10,11,12,13,14,15,17,20,21,22,23,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,70,71,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,92,93,94,95,96,97,98,99,100,101,102,103,105,108,109,112,113,114,115,116,117,118,119,121,122,123,125,126,127,128,129,130,],[21,21,-1,-4,-5,-6,-7,21,-11,21,21,-51,-41,21,21,-49,-50,-52,21,-2,-3,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-45,21,-8,-9,21,-13,-15,-20,21,21,21,21,21,21,21,21,21,21,21,21,21,-47,21,21,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-10,-12,-14,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,21,21,-62,21,-53,-54,-42,-43,-44,21,21,21,-61,-57,-59,-60,21,-58,]),'INTNUM':([0,1,2,4,5,6,7,10,11,12,13,14,15,17,20,21,22,23,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,70,71,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,92,93,94,95,96,97,98,99,100,101,102,103,105,108,109,112,113,114,115,116,117,118,119,121,122,123,125,126,127,128,129,130,],[22,22,-1,-4,-5,-6,-7,22,-11,22,22,-51,-41,22,22,-49,-50,-52,22,-2,-3,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-45,22,-8,-9,22,-13,-15,-20,22,22,22,22,22,22,22,22,22,22,22,22,22,-47,22,22,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-10,-12,-14,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,22,22,-62,22,-53,-54,-42,-43,-44,22,22,22,-61,-57,-59,-60,22,-58,]),'STRING':([0,1,2,4,5,6,7,10,11,12,13,14,15,17,20,21,22,23,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,70,71,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,92,93,94,95,96,97,98,99,100,101,102,103,105,108,109,112,113,114,115,116,117,118,119,121,122,123,125,126,127,128,129,130,],[23,23,-1,-4,-5,-6,-7,23,-11,23,23,-51,-41,23,23,-49,-50,-52,23,-2,-3,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-45,23,-8,-9,23,-13,-15,-20,23,23,23,23,23,23,23,23,23,23,23,23,23,-47,23,23,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-10,-12,-14,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,23,23,-62,23,-53,-54,-42,-43,-44,23,23,23,-61,-57,-59,-60,23,-58,]),'IF':([0,1,2,4,5,6,7,11,12,14,15,21,22,23,28,29,44,46,47,49,50,51,52,67,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,92,93,94,95,96,97,98,99,100,101,102,103,105,108,113,115,116,117,118,119,121,122,123,125,126,127,128,129,130,],[24,24,-1,-4,-5,-6,-7,-11,24,-51,-41,-49,-50,-52,-2,-3,-45,-8,-9,24,-13,-15,-20,-47,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-10,-12,-14,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,-62,-53,-54,-42,-43,-44,24,24,24,-61,-57,-59,-60,24,-58,]),'WHILE':([0,1,2,4,5,6,7,11,12,14,15,21,22,23,28,29,44,46,47,49,50,51,52,67,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,92,93,94,95,96,97,98,99,100,101,102,103,105,108,113,115,116,117,118,119,121,122,123,125,126,127,128,129,130,],[25,25,-1,-4,-5,-6,-7,-11,25,-51,-41,-49,-50,-52,-2,-3,-45,-8,-9,25,-13,-15,-20,-47,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-10,-12,-14,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,-62,-53,-54,-42,-43,-44,25,25,25,-61,-57,-59,-60,25,-58,]),'FOR':([0,1,2,4,5,6,7,11,12,14,15,21,22,23,28,29,44,46,47,49,50,51,52,67,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,92,93,94,95,96,97,98,99,100,101,102,103,105,108,113,115,116,117,118,119,121,122,123,125,126,127,128,129,130,],[26,26,-1,-4,-5,-6,-7,-11,26,-51,-41,-49,-50,-52,-2,-3,-45,-8,-9,26,-13,-15,-20,-47,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-10,-12,-14,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,-62,-53,-54,-42,-43,-44,26,26,26,-61,-57,-59,-60,26,-58,]),'PRINT':([0,1,2,4,5,6,7,11,12,14,15,21,22,23,28,29,44,46,47,49,50,51,52,67,74,75,76,77,78,79,80,81,82,83,84,85,86,87,91,92,93,94,95,96,97,98,99,100,101,102,103,105,108,113,115,116,117,118,119,121,122,123,125,126,127,128,129,130,],[27,27,-1,-4,-5,-6,-7,-11,27,-51,-41,-49,-50,-52,-2,-3,-45,-8,-9,27,-13,-15,-20,-47,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-10,-12,-14,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,-62,-53,-54,-42,-43,-44,27,27,27,-61,-57,-59,-60,27,-58,]),'$end':([1,2,4,5,6,7,11,28,29,46,47,50,91,92,113,126,127,128,130,],[0,-1,-4,-5,-6,-7,-11,-2,-3,-8,-9,-13,-10,-12,-62,-57,-59,-60,-58,]),'+':([3,14,15,21,22,23,44,48,52,64,67,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,115,116,117,118,119,120,124,125,],[30,-51,-41,-49,-50,-52,-45,30,-20,30,-47,30,-16,-17,-18,-19,-21,-22,-23,-24,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-46,30,30,-48,30,30,-53,-54,-42,-43,-44,30,30,30,]),'*':([3,14,15,21,22,23,44,48,52,64,67,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,115,116,117,118,119,120,124,125,],[32,-51,-41,-49,-50,-52,-45,32,-20,32,-47,32,32,32,-18,-19,32,32,-23,-24,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-46,32,32,-48,32,32,-53,-54,-42,-43,-44,32,32,32,]),'/':([3,14,15,21,22,23,44,48,52,64,67,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,115,116,117,118,119,120,124,125,],[33,-51,-41,-49,-50,-52,-45,33,-20,33,-47,33,33,33,-18,-19,33,33,-23,-24,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-46,33,33,-48,33,33,-53,-54,-42,-43,-44,33,33,33,]),'DOTADD':([3,14,15,21,22,23,44,48,52,64,67,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,115,116,117,118,119,120,124,125,],[34,-51,-41,-49,-50,-52,-45,34,-20,34,-47,34,-16,-17,-18,-19,-21,-22,-23,-24,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-46,34,34,-48,34,34,-53,-54,-42,-43,-44,34,34,34,]),'DOTSUB':([3,14,15,21,22,23,44,48,52,64,67,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,115,116,117,118,119,120,124,125,],[35,-51,-41,-49,-50,-52,-45,35,-20,35,-47,35,-16,-17,-18,-19,-21,-22,-23,-24,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-46,35,35,-48,35,35,-53,-54,-42,-43,-44,35,35,35,]),'DOTMUL':([3,14,15,21,22,23,44,48,52,64,67,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,115,116,117,118,119,120,124,125,],[36,-51,-41,-49,-50,-52,-45,36,-20,36,-47,36,36,36,-18,-19,36,36,-23,-24,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-46,36,36,-48,36,36,-53,-54,-42,-43,-44,36,36,36,]),'DOTDIV':([3,14,15,21,22,23,44,48,52,64,67,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,115,116,117,118,119,120,124,125,],[37,-51,-41,-49,-50,-52,-45,37,-20,37,-47,37,37,37,-18,-19,37,37,-23,-24,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-46,37,37,-48,37,37,-53,-54,-42,-43,-44,37,37,37,]),'>':([3,14,15,21,22,23,44,48,52,64,67,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,115,116,117,118,119,120,124,125,],[38,-51,-41,-49,-50,-52,-45,38,-20,38,-47,38,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,38,38,38,38,38,38,38,38,38,38,38,38,-46,38,38,-48,38,38,-53,-54,-42,-43,-44,38,38,38,]),'<':([3,14,15,21,22,23,44,48,52,64,67,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,115,116,117,118,119,120,124,125,],[39,-51,-41,-49,-50,-52,-45,39,-20,39,-47,39,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,39,39,39,39,39,39,39,39,39,39,39,39,-46,39,39,-48,39,39,-53,-54,-42,-43,-44,39,39,39,]),'LESEQ':([3,14,15,21,22,23,44,48,52,64,67,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,115,116,117,118,119,120,124,125,],[40,-51,-41,-49,-50,-52,-45,40,-20,40,-47,40,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,40,40,40,40,40,40,40,40,40,40,40,40,-46,40,40,-48,40,40,-53,-54,-42,-43,-44,40,40,40,]),'MOREEQ':([3,14,15,21,22,23,44,48,52,64,67,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,115,116,117,118,119,120,124,125,],[41,-51,-41,-49,-50,-52,-45,41,-20,41,-47,41,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,41,41,41,41,41,41,41,41,41,41,41,41,-46,41,41,-48,41,41,-53,-54,-42,-43,-44,41,41,41,]),'NOTEQUALS':([3,14,15,21,22,23,44,48,52,64,67,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,115,116,117,118,119,120,124,125,],[42,-51,-41,-49,-50,-52,-45,42,-20,42,-47,42,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,42,42,42,42,42,42,42,42,42,42,42,42,-46,42,42,-48,42,42,-53,-54,-42,-43,-44,42,42,42,]),'EQUALS':([3,14,15,21,22,23,44,48,52,64,67,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,115,116,117,118,119,120,124,125,],[43,-51,-41,-49,-50,-52,-45,43,-20,43,-47,43,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,43,43,43,43,43,43,43,43,43,43,43,43,-46,43,43,-48,43,43,-53,-54,-42,-43,-44,43,43,43,]),"'":([3,14,15,21,22,23,44,48,52,64,67,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,115,116,117,118,119,120,124,125,],[44,-51,-41,-49,-50,-52,-45,44,-20,44,-47,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-46,44,44,-48,44,44,-53,-54,-42,-43,-44,44,44,44,]),'}':([4,5,6,7,11,12,29,46,47,49,50,51,91,92,93,113,126,127,128,130,],[-4,-5,-6,-7,-11,50,-3,-8,-9,92,-13,-15,-10,-12,-14,-62,-57,-59,-60,-58,]),'ELSE':([4,5,6,7,11,29,46,47,50,91,92,113,126,127,128,130,],[-4,-5,-6,-7,-11,-3,-8,-9,-13,-10,-12,-62,129,-59,-60,-58,]),'=':([14,15,72,115,116,],[53,58,112,-53,-54,]),'ADDASSIGN':([14,15,115,116,],[54,59,-53,-54,]),'SUBASSIGN':([14,15,115,116,],[55,60,-53,-54,]),'MULASSIGN':([14,15,115,116,],[56,61,-53,-54,]),'DIVASSIGN':([14,15,115,116,],[57,62,-53,-54,]),')':([14,15,21,22,23,44,52,64,67,74,75,76,77,78,79,80,81,82,83,84,85,86,87,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,111,115,116,117,118,119,],[-51,-41,-49,-50,-52,-45,-20,105,-47,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,117,-46,118,119,-48,121,122,-53,-54,-42,-43,-44,]),']':([14,15,20,21,22,23,44,52,67,68,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,94,95,96,97,98,99,100,101,102,103,105,108,115,116,117,118,119,120,125,],[-51,-41,67,-49,-50,-52,-45,-20,-47,108,-55,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-55,115,116,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,-53,-54,-42,-43,-44,-56,-61,]),',':([14,15,21,22,23,44,52,67,68,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,94,95,96,97,98,99,100,101,102,103,105,108,115,116,117,118,119,120,],[-51,-41,-49,-50,-52,-45,-20,-47,109,-55,109,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-55,109,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,-53,-54,-42,-43,-44,-56,]),':':([14,15,21,22,23,44,52,67,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,94,95,96,97,98,99,100,101,102,103,105,108,115,116,117,118,119,124,],[-51,-41,-49,-50,-52,-45,-20,-47,-16,-17,-18,-19,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,114,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-46,-48,-53,-54,-42,-43,-44,114,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instruction':([0,1,12,49,121,122,123,129,],[2,28,51,93,126,127,128,130,]),'expression':([0,1,10,12,13,17,20,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,49,53,54,55,56,57,58,59,60,61,62,63,65,66,70,71,109,112,114,121,122,123,129,],[3,3,48,3,52,64,69,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,3,94,95,96,97,98,99,100,101,102,103,104,106,107,110,111,120,124,125,3,3,3,3,]),'if_stmt':([0,1,12,49,121,122,123,129,],[5,5,5,5,5,5,5,5,]),'while_stmt':([0,1,12,49,121,122,123,129,],[6,6,6,6,6,6,6,6,]),'for_stmt':([0,1,12,49,121,122,123,129,],[7,7,7,7,7,7,7,7,]),'print_stmt':([0,1,12,49,121,122,123,129,],[11,11,11,11,11,11,11,11,]),'sub_matrix':([0,1,10,12,13,17,20,27,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,49,53,54,55,56,57,58,59,60,61,62,63,65,66,70,71,109,112,114,121,122,123,129,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'instructions':([12,],[49,]),'vector':([20,27,45,],[68,73,89,]),'range':([45,112,],[90,123,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instruction','program',1,'p_program','Mparser.py',36),
  ('program -> program instruction','program',2,'p_program','Mparser.py',37),
  ('instruction -> expression ;','instruction',2,'p_instruction','Mparser.py',43),
  ('instruction -> ;','instruction',1,'p_instruction','Mparser.py',44),
  ('instruction -> if_stmt','instruction',1,'p_instruction','Mparser.py',45),
  ('instruction -> while_stmt','instruction',1,'p_instruction','Mparser.py',46),
  ('instruction -> for_stmt','instruction',1,'p_instruction','Mparser.py',47),
  ('instruction -> BREAK ;','instruction',2,'p_instruction','Mparser.py',48),
  ('instruction -> CONTINUE ;','instruction',2,'p_instruction','Mparser.py',49),
  ('instruction -> RETURN expression ;','instruction',3,'p_instruction','Mparser.py',50),
  ('instruction -> print_stmt','instruction',1,'p_instruction','Mparser.py',51),
  ('instruction -> { instructions }','instruction',3,'p_instruction','Mparser.py',52),
  ('instruction -> { }','instruction',2,'p_instruction','Mparser.py',53),
  ('instructions -> instructions instruction','instructions',2,'p_instructions','Mparser.py',59),
  ('instructions -> instruction','instructions',1,'p_instructions','Mparser.py',60),
  ('expression -> expression + expression','expression',3,'p_expression','Mparser.py',66),
  ('expression -> expression - expression','expression',3,'p_expression','Mparser.py',67),
  ('expression -> expression * expression','expression',3,'p_expression','Mparser.py',68),
  ('expression -> expression / expression','expression',3,'p_expression','Mparser.py',69),
  ('expression -> - expression','expression',2,'p_expression','Mparser.py',70),
  ('expression -> expression DOTADD expression','expression',3,'p_expression','Mparser.py',71),
  ('expression -> expression DOTSUB expression','expression',3,'p_expression','Mparser.py',72),
  ('expression -> expression DOTMUL expression','expression',3,'p_expression','Mparser.py',73),
  ('expression -> expression DOTDIV expression','expression',3,'p_expression','Mparser.py',74),
  ('expression -> expression > expression','expression',3,'p_expression','Mparser.py',75),
  ('expression -> expression < expression','expression',3,'p_expression','Mparser.py',76),
  ('expression -> expression LESEQ expression','expression',3,'p_expression','Mparser.py',77),
  ('expression -> expression MOREEQ expression','expression',3,'p_expression','Mparser.py',78),
  ('expression -> expression NOTEQUALS expression','expression',3,'p_expression','Mparser.py',79),
  ('expression -> expression EQUALS expression','expression',3,'p_expression','Mparser.py',80),
  ('expression -> ID = expression','expression',3,'p_expression','Mparser.py',81),
  ('expression -> ID ADDASSIGN expression','expression',3,'p_expression','Mparser.py',82),
  ('expression -> ID SUBASSIGN expression','expression',3,'p_expression','Mparser.py',83),
  ('expression -> ID MULASSIGN expression','expression',3,'p_expression','Mparser.py',84),
  ('expression -> ID DIVASSIGN expression','expression',3,'p_expression','Mparser.py',85),
  ('expression -> sub_matrix = expression','expression',3,'p_expression','Mparser.py',86),
  ('expression -> sub_matrix ADDASSIGN expression','expression',3,'p_expression','Mparser.py',87),
  ('expression -> sub_matrix SUBASSIGN expression','expression',3,'p_expression','Mparser.py',88),
  ('expression -> sub_matrix MULASSIGN expression','expression',3,'p_expression','Mparser.py',89),
  ('expression -> sub_matrix DIVASSIGN expression','expression',3,'p_expression','Mparser.py',90),
  ('expression -> sub_matrix','expression',1,'p_expression','Mparser.py',91),
  ('expression -> EYE ( expression )','expression',4,'p_expression','Mparser.py',92),
  ('expression -> ZEROS ( expression )','expression',4,'p_expression','Mparser.py',93),
  ('expression -> ONES ( expression )','expression',4,'p_expression','Mparser.py',94),
  ("expression -> expression '",'expression',2,'p_expression','Mparser.py',95),
  ('expression -> ( expression )','expression',3,'p_expression','Mparser.py',96),
  ('expression -> [ ]','expression',2,'p_expression','Mparser.py',97),
  ('expression -> [ vector ]','expression',3,'p_expression','Mparser.py',98),
  ('expression -> FLOATNUM','expression',1,'p_expression','Mparser.py',99),
  ('expression -> INTNUM','expression',1,'p_expression','Mparser.py',100),
  ('expression -> ID','expression',1,'p_expression','Mparser.py',101),
  ('expression -> STRING','expression',1,'p_expression','Mparser.py',102),
  ('sub_matrix -> expression [ vector ]','sub_matrix',4,'p_expression','Mparser.py',103),
  ('sub_matrix -> expression [ range ]','sub_matrix',4,'p_expression','Mparser.py',104),
  ('vector -> expression','vector',1,'p_expression','Mparser.py',105),
  ('vector -> vector , expression','vector',3,'p_expression','Mparser.py',106),
  ('if_stmt -> IF ( expression ) instruction','if_stmt',5,'p_if_stmt','Mparser.py',112),
  ('if_stmt -> IF ( expression ) instruction ELSE instruction','if_stmt',7,'p_if_stmt','Mparser.py',113),
  ('while_stmt -> WHILE ( expression ) instruction','while_stmt',5,'p_while_stmt','Mparser.py',119),
  ('for_stmt -> FOR ID = range instruction','for_stmt',5,'p_for_stmt','Mparser.py',125),
  ('range -> expression : expression','range',3,'p_for_stmt','Mparser.py',126),
  ('print_stmt -> PRINT vector ;','print_stmt',3,'p_print_stmt','Mparser.py',132),
]
