def set_priority(value, **kwargs):
    return {"priority": value}


def send_reply(reply_id, **kwargs):
    # Fake rest api call
    print(f"The following email model was automatically sent: {reply_id}")