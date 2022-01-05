from hashlib import md5
from django.http import Http404

from .repository import URLRepository

url_repository = URLRepository()


class URLController:
    def get_urls_by_user_pk(self, user_pk: int) -> object:
        """
            Method to get all user shortened links
        """
        return url_repository.read(author_id=user_pk)

    def get_full_url(self, url_slug: 'shorted_url') -> 'url':
        """
            Method for obtaining a full link
        """
        try:
            __url = url_repository.read(shorted_url=url_slug)
            return __url.first().full_url
        except AttributeError:
            raise Http404()

    def create_new_url(self, full_url: 'url', author_id=None) -> 'url':
        """
            Method for creating a new link
        """
        try:
            _potential_url = url_repository.read(full_url=full_url)
            return _potential_url.first().shorted_url
        except AttributeError:
            _url_hash = md5(full_url.encode()).hexdigest()[:5]
            _url = url_repository.create(shorted_url=_url_hash,
                                         full_url=full_url,
                                         author_id=author_id)
            return _url.shorted_url
