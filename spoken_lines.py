import events.timings as frequency

GREETING = """
<@{user_id}>```
Czy ktoś coś mówił o piciu? Polewaj ale pijemy co {queue_frequency_minutes} minut coby to nikt z krzesła nie spadł.


Jak bedziesz gotowy to zareaguj
👇
```""".format(
    queue_frequency_minutes=frequency.Queue().minutes,
    user_id="{user_id}")

ALREADY_STARTED = """```
Picie się już zaczęło
```"""

FAREWELL = """```
👋 Kończymy na dzisiaj.
Od: {beginning_time}
Do: {finishing_time}
Kolejek: {queues_total}
```"""

FAREWELL_NO_QUEUES = """```
👋 Dzisiaj nie pijemy w takim razie
```"""

TIMEOUT = """```
Trochę czasu upłynęło, napisz jak się namyślisz
```"""

QUEUE = """
<@{user_id}>
```
Zaczynamy {started_queue_number} kolejkę. Następna będzie za {queue_frequency_minutes} min.

Zareaguj jak wypijesz
👇
```"""

TAKEN = """```
{queue_taken} shot wypity. Kolejny o {time}
```"""
