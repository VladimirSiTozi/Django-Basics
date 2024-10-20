from datetime import datetime
from django import template


register = template.Library()


# custom simple tag
@register.simple_tag(name='current_time')
def current_time(format_string='%Y-%m-%d %H:%M:%S'):
    return datetime.now().strftime(format_string)
