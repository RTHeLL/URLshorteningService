from hashlib import md5

from django.shortcuts import get_object_or_404

from main.models import URL


class URLController:
    def get_urls_by_user_pk(self, user_pk: int) -> object:
        """
            Method to get all user shortened links
        """
        user_urls = URL.objects.filter(author_id=user_pk)
        return user_urls

    def get_full_url(self, url_slug: 'shorted_url') -> 'full_url':
        """
            Method for obtaining a full link
        """
        _url = get_object_or_404(URL, shorted_url=url_slug)
        return _url.full_url

    def get_or_create_url(self, full_url: 'url', author_id=None) -> 'shorted_url':
        """
            Method for creating a new link
        """
        _url_hash = md5(full_url.encode()).hexdigest()[:5]
        _url, _created = URL.objects.get_or_create(full_url=full_url,
                                                   defaults={'shorted_url': _url_hash,
                                                             'author_id': author_id})
        return _url.shorted_url
