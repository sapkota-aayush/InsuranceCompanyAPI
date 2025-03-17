import bleach


def sanitize(data):
    if isinstance(data,dict):
        return {key:sanitize(value) for key, value in data.items()}
    
    if isinstance(data,list):
        return {sanitize(value) for key, value in data.items()}
    
    if isinstance(data,str):
        return bleach.clean(data)
    
    return data