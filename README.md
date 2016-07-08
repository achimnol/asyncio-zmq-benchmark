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
