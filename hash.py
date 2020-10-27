import hashlib
import arrow 
user_id = "nao"
session_id = user_id + str(arrow.now())
print(session_id)
result = hashlib.md5(session_id.encode("utf-8")).hexdigest()
print(result)
