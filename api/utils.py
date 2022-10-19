from random import choices

from LinkerX.settings import URL_LETTERS
from .models import Link


def create_custom_url(length: int) -> str:
    custom_url = ''.join(choices(URL_LETTERS, k=length))
    link = Link.objects.filter(custom_url=custom_url)

    while link:
        custom_url = ''.join(choices(URL_LETTERS, k=length))
        link = Link.objects.filter(custom_url=custom_url)
    return custom_url
