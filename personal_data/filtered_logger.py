#!/bin/usr/env python3
"""
Write a function called filter_datum
that returns the log message obfuscated
"""
import logging
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Try one
    """
    logging.basicConfig(level=logging.DEBUG,
                        format='%(message)s')
    for field_name in fields:
        P = f"(?<={field_name}=)(.*?)(?={separator})"
        res = re.sub(P, redaction, message)
    return logging.debug(res)
