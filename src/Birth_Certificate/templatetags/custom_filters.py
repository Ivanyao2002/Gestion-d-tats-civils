import datetime
from django import template

register = template.Library()

MONTHS = [
    "janvier", "février", "mars", "avril", "mai", "juin",
    "juillet", "août", "septembre", "octobre", "novembre", "décembre"
]

DAYS = {
    1: "premier", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq",
    6: "six", 7: "sept", 8: "huit", 9: "neuf", 10: "dix",
    11: "onze", 12: "douze", 13: "treize", 14: "quatorze", 15: "quinze",
    16: "seize", 17: "dix-sept", 18: "dix-huit", 19: "dix-neuf", 20: "vingt",
    21: "vingt et un", 22: "vingt-deux", 23: "vingt-trois", 24: "vingt-quatre", 25: "vingt-cinq",
    26: "vingt-six", 27: "vingt-sept", 28: "vingt-huit", 29: "vingt-neuf", 30: "trente", 31: "trente et un"
}

UNITS = ["", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf"]
TENS = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante-dix", "quatre-vingt",
        "quatre-vingt-dix"]
SPECIAL_NUMBERS = {71: "soixante et onze", 81: "quatre-vingt-un", 91: "quatre-vingt-onze"}


def convert_year_to_french(year):
    if year < 1000 or year > 9999:
        raise ValueError("Year out of range (1000-9999)")

    def convert_hundred(n):
        if n == 0:
            return ""
        elif n == 1:
            return "cent"
        else:
            return UNITS[n] + " cent"

    def convert_below_hundred(n):
        if n in SPECIAL_NUMBERS:
            return SPECIAL_NUMBERS[n]
        elif n < 10:
            return UNITS[n]
        elif n < 20:
            return \
                ["dix", "onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"][
                    n - 10]
        else:
            ten = TENS[n // 10]
            unit = UNITS[n % 10]
            if unit == "":
                return ten
            elif n // 10 == 7 or n // 10 == 9:
                return TENS[n // 10 - 1] + "-" + convert_below_hundred(n % 10 + 10)
            else:
                return ten + "-" + unit

    thousands = year // 1000
    if thousands == 1:
        thousands_str = "mille"
    else:
        thousands_str = UNITS[thousands] + " mille"

    hundreds = convert_hundred((year % 1000) // 100)
    below_hundred = convert_below_hundred(year % 100)

    return f"{thousands_str} {hundreds} {below_hundred}".strip()


@register.filter(name='date_to_french_string')
def convert_date_to_french_string(date):
    day = DAYS[date.day]
    month = MONTHS[date.month - 1]
    year = convert_year_to_french(date.year)

    return f"{day} {month} {year}"


def convert_time_to_french(time):
    hours = time.hour
    minutes = time.minute

    # Convertir les heures en format texte
    if hours == 0:
        hours_str = "minuit"
    elif hours == 12:
        hours_str = "midi"
    elif hours <= 19:
        hours_str = \
            ["une", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize",
             "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"][hours - 1]
    else:
        hours_str = \
            ["vingt", "vingt et une", "vingt deux", "vingt trois", "vingt quatre", "vingt cinq", "vingt six",
             "vingt sept",
             "vingt huit", "vingt neuf"][hours - 20]

    # Convertir les minutes en format texte
    if minutes == 0:
        minutes_str = "zéro minute"
    elif minutes == 1:
        minutes_str = "une minute"
    elif minutes <= 19:
        minutes_str = \
            ["une", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize",
             "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"][minutes - 1] + " minutes"
    else:
        tens = ["vingt", "trente", "quarante", "cinquante"][(minutes // 10) - 2]
        units = ["un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf"][(minutes % 10) - 1]
        minutes_str = tens + "-" + units

    # Construction de la phrase complète
    if minutes == 0:
        return f"{hours_str} Heure(s)"
    else:
        return f"{hours_str} Heure(s) {minutes_str}"


@register.filter(name='time_to_french_string')
def convert_time_to_french_string(time):
    return convert_time_to_french(time)
