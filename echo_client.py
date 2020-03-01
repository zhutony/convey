#!/usr/bin/env python3
# Echo server program
import sys
import time
import asyncio

if len(sys.argv) < 3:
    print('missing HOST and PORT')
    exit(1)
HOST = sys.argv[1]
PORT = int(sys.argv[2])

sleep = 5 if len(sys.argv) < 4 else float(sys.argv[3])
message = 'Hello World!' if len(sys.argv) < 5 else sys.argv[4]

async def tcp_echo_client(message, loop):
    i = 0
    try:
        while True:
            reader, writer = await asyncio.open_connection(HOST, PORT, loop=loop)
            i += 1
            msg = message + ' - ' + str(i)
            print('Send: %r' % msg)
            writer.write(msg.encode())
    
            try:
                data = await reader.read(100)
            except Exception as ex:
                print("*** Error: ", ex)
                continue
    
            print('Received: %r' % data.decode())
    
            writer.close()
            time.sleep(sleep)
    except KeyboardInterrupt:
        pass

loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()
