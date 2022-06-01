

def validate_fields_existence(data, req_keys):
    for k in req_keys:
        if k not in data:
            print("%s is missing" % k)
            return False
    return True


def validate_createPrivateView_data(data):
    req_keys = ["description", "recipients", "table", "isTable", "hasHeader", "rows", "cols"]
    return validate_fields_existence(data, req_keys)


def validate_updateView(data):
    req_keys = ["viewId", "viewServer", "table"]
    return validate_fields_existence(data, req_keys)
