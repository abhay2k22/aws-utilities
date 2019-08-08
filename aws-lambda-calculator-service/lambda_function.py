import json

def lambda_handler(event, context):
    print('Received event: ')
    print(event)
    a = float(event['a'])
    b = float(event['b'])
    op = event['op']
    if a is None:
        callback("400 Invalid Input")
    if b is None:
        callback("400 Invalid Input")
    if op is None:
       callback("400 Invalid Input")

    if op == "add":
        return responseAPI(add(a,b))
    if op == "div":
        return responseAPI(div(a,b))
    if op == "mul":
        return responseAPI(mul(a,b))
    if op == "minus":
        return responseAPI(minus(a,b))
    return {
        'statusCode': 200,
        'body': "No Operation defined"
    }

def callback(msg):
    return {
        'statusCode': 400,
        'body': json.dumps(msg)
    }

def responseAPI(res):
    return {
        'statusCode': 200,
        'result': res
    }

def add(a,b):
    return a+b

def div(a,b):
    return a/b

def mul(a,b):
    return a*b

def minus(a,b):
    return a-b
