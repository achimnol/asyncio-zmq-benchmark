# AsyncIO-based ZeroMQ Benchmarks
A simple benchmark suite to compare the performance of a various combination of asyncio event loop and zeromq implementations.

An example run with Python 3.5.1, Tornado 3.4, uvloop 0.4.33, PyZMQ 15.3.0, aiozmq 0.7.1 on MacOS X 10.11 (64bit) results in:
```
asyncio + aiozmq: 0.388407 sec.
tornado + aiozmq: 0.501667 sec.
uvloop + aiozmq: 0.214249 sec.
zmqloop + pyzmq: 1.406731 sec.
tornado + pyzmq: 2.261831 sec.
```
