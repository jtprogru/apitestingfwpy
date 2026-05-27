"""
Локальный мок сервиса https://restful-api.dev для прогона тестов
без обращения к публичному API (лимит 100 запросов / IP / день).

Запуск: uv run --group mock uvicorn mock_service.main:app --host 0.0.0.0 --port 8000
"""

from datetime import datetime, timezone
from itertools import count
from typing import Any

from fastapi import FastAPI, HTTPException, status

app = FastAPI(title="restful-api.dev mock", version="0.1.0")

_storage: dict[str, dict[str, Any]] = {}
_id_seq = count(1)


def _now_iso() -> str:
    """Текущее UTC-время в формате ISO 8601 с миллисекундами."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")


@app.get("/health")
def health() -> dict[str, str]:
    """Healthcheck для контейнера и compose."""
    return {"status": "ok"}


@app.get("/objects")
def list_objects() -> list[dict[str, Any]]:
    """Список всех созданных объектов."""
    return list(_storage.values())


@app.post("/objects")
def create_object(payload: dict[str, Any]) -> dict[str, Any]:
    """Создать новый объект и присвоить ему автоинкрементный id."""
    object_id = str(next(_id_seq))
    obj = {
        "id": object_id,
        "name": payload.get("name"),
        "data": payload.get("data"),
        "createdAt": _now_iso(),
    }
    _storage[object_id] = obj
    return obj


@app.get("/objects/{object_id}")
def get_object(object_id: str) -> dict[str, Any]:
    """Получить объект по id; 404, если не найден."""
    obj = _storage.get(object_id)
    if obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found")
    return obj


@app.put("/objects/{object_id}")
def full_update_object(object_id: str, payload: dict[str, Any]) -> dict[str, Any]:
    """Полная замена объекта по id."""
    if object_id not in _storage:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found")
    obj = {
        "id": object_id,
        "name": payload.get("name"),
        "data": payload.get("data"),
        "updatedAt": _now_iso(),
    }
    _storage[object_id] = obj
    return obj


@app.patch("/objects/{object_id}")
def partial_update_object(object_id: str, payload: dict[str, Any]) -> dict[str, Any]:
    """Частичное обновление: непереданные поля сохраняются, data мерджится по ключам."""
    obj = _storage.get(object_id)
    if obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found")

    if "name" in payload:
        obj["name"] = payload["name"]
    if "data" in payload and isinstance(payload["data"], dict):
        existing_data = obj.get("data") or {}
        merged = {**existing_data, **payload["data"]}
        obj["data"] = merged

    obj["updatedAt"] = _now_iso()
    _storage[object_id] = obj
    return obj


@app.delete("/objects/{object_id}")
def delete_object(object_id: str) -> dict[str, str]:
    """Удалить объект по id; 404, если уже нет."""
    if object_id not in _storage:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Object not found")
    del _storage[object_id]
    return {"message": f"Object with id = {object_id} has been deleted."}
