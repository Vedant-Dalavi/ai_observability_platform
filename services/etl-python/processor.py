import json

def clean_log(raw_msg: bytes):
    data = json.loads(raw_msg.decode("utf-8"))

    cleaned = {
        "id": data.get("id"),
        "service": data.get("service"),
        "level": data.get("level"),
        "message": data.get("message"),
        "timestamp": data.get("timestamp")
    }

    return cleaned
