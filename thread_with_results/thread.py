#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
xray.py

Source code : https://github.com/yang445786754/thread-with-results

Author :

* Tony_9410 - tony_9410@foxmail.com

"""

from threading import Thread
from traceback import format_exc
import inspect
import ctypes


def __async_raise(tid, exctype):
    if not inspect.isclass(exctype):
        raise TypeError("Only types can be raised (not instances)")
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(tid), ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread, safe=True):
    try:
        __async_raise(thread.ident, SystemExit)
    except ValueError as E:
        if not safe:
            raise E


class ThreadWithResult(Thread):
    """
    can get the results with call call x.results
    """
    def __init__(self, func=None, *args, **kwargs):
        super().__init__()
        self._func = func
        self._args = args
        self._kwargs = kwargs

        self._error = ''
        self._timeout = True
        self._done = False
        self._results = None

    def run(self) -> None:
        try:
            if self._func is not None:
                self._results = self._func(*self._args, **self._kwargs)
            self._done = True
        except Exception:
            self._error = format_exc()
        else:
            self._done = True
        finally:
            self._timeout = False
            del self._func, self._args, self._kwargs

    @property
    def results(self):
        return self._results

    @property
    def done(self):
        return self._done

    @property
    def error(self):
        return self._error

    @property
    def timeout(self):
        return self._timeout

    def _wait_for_tstate_lock(self, block=True, timeout=-1):
        lock = self._tstate_lock
        if lock is None:
            assert self._is_stopped
            return

        try:
            if lock.acquire(block, timeout):
                lock.release()
                self._stop()
        except Exception as E:
            if lock.locked():
                lock.release()
                self._stop()
            raise

    def stop_thread(self, safe=True):
        stop_thread(self, safe=safe)
