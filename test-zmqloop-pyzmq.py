import asyncio
import zmq.asyncio
import time
import os

zmq.asyncio.install()
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
    poller = zmq.asyncio.Poller()
    poller.register(client, zmq.POLLIN)
    with open(os.devnull, 'w') as null:
        while True:
            events = await poller.poll()
            if client in dict(events):
                greeting = await client.recv_multipart()
                if greeting[0] == b'exit': break
                print(greeting[0], file=null)

def main():
    loop = asyncio.get_event_loop()
    loop.create_task(pushing())
    try:
        begin = time.monotonic()
        loop.run_until_complete(pulling())
        end = time.monotonic()
        print('zmqloop + pyzmq: {:.6f} sec.'.format(end - begin))
    except KeyboardInterrupt:
        loop.stop()
    loop.close()

if __name__ == '__main__':
    main()

