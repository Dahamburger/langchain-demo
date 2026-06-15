import redis
try:
    print(redis.__version__)
except Exception as e:
    print(e)