import asyncio
import struct
from constants import *
from commands import *

MAX_CONNECTION = 10
active_connections = []

async def client_handler(reader,writer):
    global active_connections
    active_connections.append(writer)

    addr = writer.get_extra_info('peername')
    print (f'Connected to {addr}. Current active connections = {len(active_connections)}')

    connected=True
    
    while connected:
        # read from client
        msg = await reader.read(16)
        if len(msg) == 16 :
            (command,p1,p2,p3) = struct.unpack('IIII',msg)
        else:
            command = commandCode._PI_CMD_NC

        match command:
            case commandCode._PI_CMD_BR1: #blank read
                writer.write(blankRead())
                await writer.drain()

            case commandCode._PI_CMD_HWVER: #get hardware version
                writer.write(getHwVersion(command,p1,p2))
                await writer.drain()

            case commandCode._PI_CMD_MODES: #set mode
                writer.write(setMode(command,p1,p2))
                await writer.drain()

            case commandCode._PI_CMD_MODEG: #get mode
                writer.write(getMode(command,p1,p2))
                await writer.drain()

            case commandCode._PI_CMD_WRITE: #write level
                writer.write(writeDigital(command,p1,p2))
                await writer.drain()

            case commandCode._PI_CMD_READ: #read level
                writer.write(readDigital(command,p1,p2))
                await writer.drain()

            case commandCode._PI_CMD_PUD:
                writer.write(setPullUpDown(command,p1,p2))
                await writer.drain()

            case commandCode._PI_CMD_NC:
                writer.close()
                await writer.wait_closed()
                connected=False
                active_connections = [x for x in active_connections if x!=writer]
                print('connection closed')

            case _: #default response success
                writer.write(defaultResponse(command,p1,p2))
                await writer.drain()

async def manage_connections():
    global active_connections

    while True:
        if(len(active_connections)>MAX_CONNECTION):
            oldest = active_connections[0]
            #print(f'Removing oldest connection instance {oldest.get_extra_info('peername')}')

            oldest.close()
            await oldest.wait_closed()
            active_connections.pop(0)

        await asyncio.sleep(1)

async def run_server(host='127.0.0.1',port=8888):
    if init()==0:
        print('Cannot start wiringpi initialization')
        return
    
    # Bind to localhost on port 8888
    server = await asyncio.start_server(client_handler, host, port)
    
    asyncio.create_task(manage_connections())

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    
    # Keep the server running until stopped
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(run_server('0.0.0.0',8888))