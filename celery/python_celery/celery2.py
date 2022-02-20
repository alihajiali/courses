from celery1 import add
add.apply_async(args=[5, 8])

# or

add.delay(5, 8)