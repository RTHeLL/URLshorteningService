from main.models import URL


class URLRepository:
    def create(self, **kwargs) -> object:
        """
            Method for adding a new object to the URL table
        """
        try:
            _new_url_object = URL(**kwargs)
            _new_url_object.save()
            return _new_url_object
        except ValueError:
            pass  # todo add treatment

    def read(self, **kwargs) -> 'QuerySet':
        """
            Method to read from URL table
        """
        try:
            _urls_object = URL.objects.filter(**kwargs)
            return _urls_object
        except ValueError:
            pass  # todo add treatment
