import re

thousands = '(M{0,3})'
hundreds = '(C[DM]|D?C{0,3})'
tens = '(X[CL]|L?X{0,3})'
digits = '(I[VX]|V?I{0,3})'

regex_pattern = r'{0}{1}{2}{3}$'.format(thousands, hundreds, tens, digits)

print(str(bool(re.match(regex_pattern, input()))))
