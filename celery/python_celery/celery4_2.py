from socket import timeout
from celery4_1 import add

result = add.delay(5, 8)

print(result)         #   UUID

print(result.ready())    #   bool(ایا جواب اماده است ؟)
print(result.get(timeout=2))   #  ۲ ثانیه صبر میکنه اگر جواب حاضر نبود ارور میده

print(result.get())   #   صبر میکنه تا جپاب اماده بشه