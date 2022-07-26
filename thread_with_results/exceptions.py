#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ThreadWithResultsError(Exception):
    """
    Exception error class for ThreadWithResultsError class

    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

    def __repr__(self):
        return f"ThreadWithResultsError exception {self.value}"


class ThreadWithResultsTimeout(ThreadWithResultsError):
    """
    Exception error class for ThreadWithResultsTimeout class

    """


class ThreadWithResultsTypeError(ThreadWithResultsError):
    """
    Exception error class for ThreadWithResultsTypeError class

    """
