import websockets, asyncio, threading, time, pprint

def ping(ws):
    async def send_msg(msg):
        await ws.send(msg)

    while True:
        asyncio.run(send_msg("3"))
        time.sleep(10)
    
async def ws_handler():
    async with websockets.connect("wss://frontend-api.pump.fun/socket.io/?EIO=4&transport=websocket") as ws:
        await ws.send("40")
        threading.Thread(target=ping, args=(ws,)).start()
        while True:
            msg = await ws.recv()
            pprint.pprint(f"Received: {msg}")

if __name__ == "__main__":
    asyncio.run(ws_handler())