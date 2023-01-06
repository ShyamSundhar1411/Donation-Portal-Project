from django import template
import datetime
from services.choices import COMPATBILE_TYPES

register = template.Library()

def age(bday, d=None):
    if d is None:
        d = datetime.date.today()
    return (d.year - bday.year) - int((d.month, d.day) < (bday.month, bday.day))
def split(strings,key):
    for i in COMPATBILE_TYPES:
        if i[0] == strings:
            return i[-1].split(key)
register.filter('age', age)
register.filter("split",split)