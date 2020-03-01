#!/usr/bin/env python3
import sys
import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print("Received %r from %r" % (message, addr))

    print("Send: %r" % message)
    writer.write(data)
    await writer.drain()

    print("Close the client socket")
    writer.close()

if len(sys.argv) < 3:
    print('{0} IP Port'.format(sys.argv[0]))
    sys.exit()

bindIp = sys.argv[1]
bindPort = int(sys.argv[2])

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, bindIp, bindPort, loop=loop)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
