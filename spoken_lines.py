from datetime import date
import time


GREETING = """```
No i to mi się podoba. Pijemy nie śpimy, polewaj i pijemy co 15 minutek co by to nikt z krzesła nie spadł.


Jak bedziesz gotowy to zareaguj
👇
```"""

ALREADY_STARTED = """```
Picie się już zaczęło
```"""

FAREWELL = """```
👋 Kończymy na dzisiaj.
{0}       
Kolejek: {1}
```""".format(str(date.today()) + time.strftime(" %H:%M"), "{0}")  # {0} to format in function

TIMEOUT = """```
Trochę czasu upłynęło, napisz jak się namyślisz
```"""

QUEUE = """
<@{1}>
```
Zaczynamy {0} kolejeczke. Następna będzie za 15 min.

Zareaguj jak wypijesz
👇
```"""

TAKEN = """```
Shot wypity
```"""
