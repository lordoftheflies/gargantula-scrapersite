from django.conf import settings


class MiddlewareException(Exception):

    def __init__(self, *args):
        super().__init__(*args)


class SplashMiddlewareException(MiddlewareException):

    def __init__(self, *args):
        super().__init__(*args)
        self.url = settings.SCRAPYD_URL

    def __str__(self):
        return 'Splash middleware[%s] exception: %s' % (
            self.url,
            self.args[0],
        )
