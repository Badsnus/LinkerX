from random import choices

from LinkerX.settings import SHORT_URL_LETTERS
from .models import Link


def create_short_link() -> str:
    short_url = ''.join(choices(SHORT_URL_LETTERS, k=5))
    link = Link.objects.filter(short_url=short_url)
    while link:
        short_url = ''.join(choices(SHORT_URL_LETTERS, k=5))
        link = Link.objects.filter(short_url=short_url)
    return short_url
