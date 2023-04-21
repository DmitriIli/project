from django import template

register = template.Library()

@register.filter()
def trunc(value):
    return f'{value}_id' 

