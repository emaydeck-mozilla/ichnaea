import logging

from pyramid.httpexceptions import HTTPError
from pyramid.response import Response

from ichnaea.decimaljson import dumps

logger = logging.getLogger('ichnaea')


class _JSONError(HTTPError):
    def __init__(self, errors, status=400):
        body = {'errors': errors}
        Response.__init__(self, dumps(body))
        self.status = status
        self.content_type = 'application/json'


def error_handler(errors):
    # filter out the rather common MSG_ONE_OF errors
    log_errors = []
    for error in errors:
        if error.get('description', '') != MSG_ONE_OF:
            log_errors.append(error)
    if log_errors:
        logger.debug('error_handler' + repr(log_errors))
    return _JSONError(errors, errors.status)


MSG_ONE_OF = 'You need to provide a mapping with least one cell or wifi entry.'
