def json_api_request(resource: str = None, attrs: dict = None):
    if not resource or not attrs:
        raise ValueError()
    req = {
        "data": {
            "type": f'{resource}',
            "attributes": attrs
        }
    }
    return req
