import asyncio
import zmq.asyncio
from tornado.ioloop import IOLoop
from tornado.platform.asyncio import AsyncIOMainLoop
import time
import os

zmq.asyncio.install()
AsyncIOMainLoop().install()
ctx = zmq.asyncio.Context()

async def pushing():
    server = ctx.socket(zmq.PUSH)
    server.bind('tcp://*:9000')
    for i in range(5000):
        await server.send(b'Hello %d' % i)
    await server.send(b'exit')

async def pulling():
    client = ctx.socket(zmq.PULL)
    client.connect('tcp://127.0.0.1:9000')
    with open(os.devnull, 'w') as null:
        while True:
            greeting = await client.recv_multipart()
            if greeting[0] == b'exit': break
            print(greeting[0], file=null)

def main():
    loop = IOLoop.current()
    loop.spawn_callback(pushing)
    try:
        begin = time.monotonic()
        loop.run_sync(pulling)
        end = time.monotonic()
        print('tornado + pyzmq: {:.6f} sec.'.format(end - begin))
    except KeyboardInterrupt:
        loop.stop()
    loop.close()

if __name__ == '__main__':
    main()

