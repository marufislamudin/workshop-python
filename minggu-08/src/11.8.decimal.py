# modul decimal 
from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)
round(.70 * 1.05, 2)

# kelas decimal untuk menghitung modulo
Decimal('1.00') % Decimal('.10')
1.00 % 0.10
sum([Decimal('0.1')]*10) == Decimal('1.0')
sum([0.1]*10) == 1.0

# modul decimal 
# menyediakan aritmatika dengan presisi sebanyak yang diperlukan
getcontext().prec = 36
Decimal(1) / Decimal(7)