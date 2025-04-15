connected_clients = []

async def broadcast_message(message: str):
    print(f"📢 Broadcasting to {len(connected_clients)} clients: {message}")
    for ws in connected_clients:
        try:
            await ws.send_text(message)
        except Exception as e:
            print("⚠️ Failed to send to a client:", e)