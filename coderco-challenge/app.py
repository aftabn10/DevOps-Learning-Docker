import os
from flask import Flask
import redis

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port)

@app.route("/")
def welcome():
    return """
    Welcome Page
    <br>
    <a href="/count">Click here to see the visit count!</a>
    """

@app.route("/count")
def count():
    visits = r.incr('visits')
    return f"""
    This page has been visited {visits} times
    <br>
    <a href="/">Go back to Homepage</a>
    """

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)