import json

response_1 = '{"detail": "Method not allowed"}'
request_obj = json.loads(response_1)
print(request_obj["detail"])