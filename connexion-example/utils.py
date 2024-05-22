import random
from datetime import datetime

def random_datetime():
    # Losowa wartość dla roku w zakresie od 2000 do 2025
    year = random.randint(2020, 2025)
    # Losowa wartość dla miesiąca w zakresie od 1 do 12
    month = random.randint(1, 12)
    # Losowa wartość dla dnia w zakresie od 1 do 28 (zakładamy uproszczenie)
    day = random.randint(1, 28)
    # Losowa wartość dla godziny w zakresie od 0 do 23
    hour = random.randint(0, 23)
    # Losowa wartość dla minuty w zakresie od 0 do 59
    minute = random.randint(0, 59)
    # Losowa wartość dla sekundy w zakresie od 0 do 59
    second = random.randint(0, 59)

    # Utworzenie obiektu daty i czasu
    random_date = datetime(year, month, day, hour, minute, second)
    return random_date