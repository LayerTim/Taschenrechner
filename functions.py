from decimal import Decimal, getcontext

# Präzision der Rechnungen in Stellen festlegen
getcontext().prec = 28

# a und b können hier float oder int sein.
# Decimal() stellt ein eigenes Zahlensystem bereit.
# Beruht auf Basis Zehnerpotenz plus Mantisse.
def add(a,b):
    da = Decimal(str(a))
    db = Decimal(str(b))
    return da + db

def sub(a,b):
    da = Decimal(str(a))
    db = Decimal(str(b))
    return da - db

def mul(a,b):
    da = Decimal(str(a))
    db = Decimal(str(b))
    return da * db

def div(a,b):
    da = Decimal(str(a))
    db = Decimal(str(b))
    return da / db