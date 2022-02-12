import datetime
from datetime import date
import time


GREETING = """<@{0}>```
Czy ktoś coś mówił o piciu? Polewaj ale pijemy co 15 minut coby to nikt z krzesła nie spadł.


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

FAREWELL_NO_QUEUES = """```
👋 Dzisiaj nie pije w takim razie
```"""

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
{0} shot wypity. Kolejny o {1}
```""".format("{0}", (datetime.datetime.now() + datetime.timedelta(minutes=15)).strftime("%H:%M:%S"))
