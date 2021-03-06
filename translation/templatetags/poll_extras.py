from django import template

register = template.Library()


@register.filter
def sort_lower(lst, key_name):
    return sorted(lst, key=lambda item: getattr(item, key_name).lower())