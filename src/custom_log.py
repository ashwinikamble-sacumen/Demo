"""This file contains custom logs."""
import logging
from typing import Any


class LoggerDemoConsole:  # pylint: disable=too-few-public-methods
    """Logger class have testlog method."""

    def testlog(self: Any) -> None:
        """Testlog method have logger object."""
        # logger = logging.getLogger('demologger')
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)
        fileHandler = logging.FileHandler("demo.log", mode="a")
        fileHandler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s%(levelname)s: %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S%p",
        )
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warn message")
        logger.error("error message")
        logger.critical("critical message")


demo = LoggerDemoConsole()
demo.testlog()
print("Done")
