import re


plural_map = {
    # singular: plural
    'metadata': 'metadata',
}


def pluralize(name):
    # Getting the name like this will break down as soon as we add
    # resources that don't just append an s for pluralization. Fix when
    # that problem arises.
    if name in plural_map:
        return plural_map[name]
    return name.lower() + 's'


def singularize(name):
    # This is a total hack that will only work with ESP resources. Don't use
    # this for anything else.
    if name[-1:] == 's':
        return name[:-1]
    return name


def underscore_to_titlecase(value):
    return ''.join(x.capitalize() for x in value.split("_"))


cap_re = re.compile(r'(.)([A-Z][a-z]+)')
all_re = re.compile(r'([a-z0-9])([A-Z])')


def titlecase_to_underscore(value):
    s1 = cap_re.sub(r'\1_\2', value)
    return all_re.sub(r'\1_\2', s1).lower()
