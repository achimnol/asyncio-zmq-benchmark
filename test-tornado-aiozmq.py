import asyncio
import zmq
import aiozmq
from tornado.ioloop import IOLoop
from tornado.platform.asyncio import AsyncIOMainLoop
import time
import os

AsyncIOMainLoop().install()

async def pushing():
    server = await aiozmq.create_zmq_stream(zmq.PUSH,
                                            bind='tcp://*:9000')
    for i in range(5000):
        server.write([b'Hello %d' % i])
    server.write([b'exit'])
    await server.drain()

async def pulling():
    client = await aiozmq.create_zmq_stream(zmq.PULL,
                                            connect='tcp://127.0.0.1:9000')
    with open(os.devnull, 'w') as null:
        while True:
            greeting = await client.read()
            if greeting[0] == b'exit': break
            print(str(greeting[0]), file=null)

def main():
    loop = IOLoop.current()
    loop.spawn_callback(pushing)
    try:
        begin = time.monotonic()
        loop.run_sync(pulling)
        end = time.monotonic()
        print('tornado + aiozmq: {:.6f} sec.'.format(end - begin))
    except KeyboardInterrupt:
        loop.stop()
    loop.close()

if __name__ == '__main__':
    main()

