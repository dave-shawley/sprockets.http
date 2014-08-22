"""
Sprockets HTTP

"""
version_info = (0, 1, 0)
__version__ = '.'.join(str(v) for v in version_info)

import logging

DEFAULT_PORT = 8000

HELP = 'HTTP Application Controller'

LOGGER = logging.getLogger(__name__)


def add_cli_arguments(parser):

    parser.add_argument('-p', '--port',
                        action='store',
                        type=int,
                        help='Port to listen on. Default: %s' % DEFAULT_PORT)


def main(app, args):
    LOGGER.debug('I would run the %s app, but I am not written yet', app)
