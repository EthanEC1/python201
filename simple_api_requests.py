import requests

req = requests.get("https://www.youtube.com/")
print(req.status_code)



# import requests
# import time
# while True:
#     req = requests.get("https://courses.codingforeverybody.com")
#     print(req.status_code)
#     if req.status_code != 200:
#         # Email me or text me
#         pass
#     time.sleep(3)    