#!/usr/bin/python3
"""Module to verify if a data set represents valid UTF-8 encoding"""


def validUTF8(data):
    """Checks if the given data set represents a valid UTF-8 encoding"""
    try:
        data = [n & 255 for n in data]
        bytes(data).decode("UTF-8")
        return True
    except Exception:
        return False
