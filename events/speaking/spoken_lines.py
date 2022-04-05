from inspect import cleandoc


GREETING = cleandoc("""<@{user_id}>
    ```
    Czy ktoś coś mówił o piciu? Polewaj ale pijemy co {queue_frequency_minutes} minut coby to nikt z krzesła nie spadł.
    
    
    Jak bedziesz gotowy to zareaguj
    👇
    ```""")

ALREADY_STARTED = cleandoc("""```
    Picie się już zaczęło
    ```""")

FAREWELL = cleandoc("""```
    👋 Kończymy na dzisiaj.
    Od: {beginning_time}
    Do: {finishing_time}
    Kolejek: {queues_total}
    ```""")

FAREWELL_NO_QUEUES = cleandoc("""```
    👋 Dzisiaj nie pijemy w takim razie
    ```""")

TIMEOUT = cleandoc("""```
    Trochę czasu upłynęło, napisz jak się namyślisz
    ```""")

QUEUE = cleandoc("""
    <@{user_id}>
    ```
    Zaczynamy {started_queue_number} kolejkę. Następna będzie za {queue_frequency_minutes} min.
    
    Zareaguj jak wypijesz
    👇
    ```""")

TAKEN = cleandoc("""```
    {queue_taken} shot wypity. Kolejny o {time}
    ```""")
