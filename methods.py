import cpi
from cpi.errors import CPIObjectDoesNotExist
from datetime import date

def _first_of_month(d):
    if hasattr(d, "date"):
        d = d.date()
    if not isinstance(d, date):
        raise TypeError("safe_cpi_get expected a date-like value.")
    if d.day != 1:
        d = d.replace(day=1)
    return d

def _previous_month(d):
    if d.month == 1:
        return date(d.year - 1, 12, 1)
    return date(d.year, d.month - 1, 1)

latest_month = cpi.LATEST_MONTH

def safe_cpi_get(d, max_lookback=24):
    if d > latest_month:
        d = latest_month
    
    last_err = None
    for _ in range(max_lookback + 1):
        try:
            return cpi.get(d)
        except CPIObjectDoesNotExist as err:
            last_err = err
            d = _previous_month(d)
    raise last_err
