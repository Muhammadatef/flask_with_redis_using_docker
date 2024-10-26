from flask import Flask
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

@app.route('/')
def count_visits():
    visits = redis_client.incr('counter')
    return f"Hello! You have visited this page {visits} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
