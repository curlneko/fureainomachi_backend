from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.services.chat_service import ChatManager

router = APIRouter()
manager = ChatManager()


@router.websocket("/{room_id}")
async def chat_websocket_endpoint(websocket: WebSocket, room_id: str) -> None:
    await manager.connect(room_id, websocket)

    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_to_room(room_id, data)
    except WebSocketDisconnect:
        manager.disconnect(room_id, websocket)
