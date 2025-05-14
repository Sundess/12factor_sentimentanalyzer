import redis

# Connect to local Redis
r = redis.Redis(host="localhost", port=6379, db=0)

# Test connection
try:
    response = r.ping()
    if response:
        print("Connected to Redis successfully!")
except redis.ConnectionError:
    print("Failed to connect to Redis!")
