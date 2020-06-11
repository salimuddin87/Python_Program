import logging
from pythonjsonlogger import jsonlogger
import sys


class MakeLogger:
    """
    This is module for logging
    """

    def __init__(self, filename):
        # Root logger for all logging
        self.root_logger = logging.getLogger(filename)
        self.root_logger.setLevel(logging.INFO)

        formatter = jsonlogger.JsonFormatter(
        '%(asctime)s %(levelname)s %(name)s %(lineno)s %(message)s'
        )

        stream_handler = logging.StreamHandler(sys.stderr)
        stream_handler.setFormatter(formatter)
        self.root_logger.addHandler(stream_handler)

    def info(self, msg, *args, **kwargs):
        self.root_logger.info(msg)

    def error(self, msg, *args, **kwargs):
        self.root_logger.error(msg)

    def warn(self, msg, *args, **kwargs):
        self.root_logger.warning(msg)

    @staticmethod
    def skip_library_logging(libraries):
        # skip libraries modules logging
        for library in libraries:
            logging.getLogger(library).setLevel(logging.ERROR)