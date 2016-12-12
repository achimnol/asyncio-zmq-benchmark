# AsyncIO-based ZeroMQ Benchmarks
A simple benchmark suite to compare the performance of a various combination of asyncio event loop and zeromq implementations.

An example run with Python 3.5.1, Tornado 4.3, uvloop 0.4.33, PyZMQ 15.3.0, aiozmq 0.7.1 on MacOS X 10.11 (64bit) results in:
```
asyncio + aiozmq: 0.363527 sec.
tornado + aiozmq: 0.418002 sec.
uvloop + aiozmq: 0.182694 sec.
zmqloop + pyzmq: 0.704048 sec.
tornado + pyzmq: 1.093527 sec.
```

Another setup with Python 3.6.0rc1, Tornado 4.4.2, uvloop 0.6.7, PyZMQ 16.0.2, aiozmq 0.7.1 on macOS 10.12 (64bit) results in:

```
asyncio + aiozmq: 0.256548 sec.
tornado + aiozmq: 0.356422 sec.
uvloop + aiozmq: 0.186459 sec.
zmqloop + pyzmq: 0.209287 sec.
tornado + pyzmq: 0.207432 sec.
```

Note that Python 3.6 has replaced asyncio's Future and Task implementations with equivalent C modules.
