from django import template
register = template.Library()

@register.filter
def get(mapping,key):
    a = mapping.get(key,'')
    print(a)
    print(a[0])
    return mapping.get(key,'')

@register.filter
def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    print(value)
    return value.lower()