from django import template

register = template.Library()

LIST_OF_BAD = (
    'редиска',
    'негодяй',
    'негодяев',
    'хитрожопый',
    'хитрожопые',
    'говнюк',
    'жопошник',
    'засранец'
)
LIST_OF_GOOD = (
    'р******',
    'н******',
    'н*******',
    'х*********',
    'х*********',
    'г*****',
    'ж*******',
    'з*******'
)


@register.filter()
def censor(value):
    for i in range(0, len(LIST_OF_BAD)):
        re1 = LIST_OF_BAD[i]
        re2 = LIST_OF_GOOD[i]

        value = value.replace(re1, '--')
        value = value.replace(re2, re1)
        value = value.replace('--', re2)
    return value
