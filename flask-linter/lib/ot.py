def applyOperation(text, operation):
    if not operation:
        return text
    result = text
    for op in operation:
        if op['text']:
            if op['action'] == "insert":
                result = result[0:op['start']] + op['text'] + result[op['start']:]
            if op['action'] == "remove":
                result = result[0:op['start']] + result[int(op['start']) + len(op['text']):]
    return result