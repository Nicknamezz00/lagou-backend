def JsonAPIRequest(type: str=None, attrs: dict=None):
    if not type or not attrs:
        raise ValueError()
    req = {
            "data": {
                "type": f'{type}',
                "attributes": attrs
            }
        }
    return req
