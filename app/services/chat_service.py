from fastapi import WebSocket

from app.core.logger import logger


class ChatManager:
    def __init__(self) -> None:
        self.active_rooms: dict[str, list[WebSocket]] = {}

    async def connect(self, room_id: str, websocket: WebSocket) -> None:
        await websocket.accept()
        if room_id not in self.active_rooms:
            self.active_rooms[room_id] = []
            logger.info(f"Created new room {room_id}")
        self.active_rooms[room_id].append(websocket)
        logger.info(f"WebSocket connected to room {room_id}")

    def disconnect(self, room_id: str, websocket: WebSocket) -> None:
        self.active_rooms[room_id].remove(websocket)
        if len(self.active_rooms[room_id]) == 0:
            del self.active_rooms[room_id]
            logger.info(f"Room {room_id} is now empty and removed")
        logger.info(f"WebSocket disconnected from room {room_id}")

    async def send_to_room(self, room_id: str, message: str) -> None:
        for ws in self.active_rooms.get(room_id, []):
            await ws.send_text(message)
        logger.info(f"Sent message to room {room_id}: {message}")
