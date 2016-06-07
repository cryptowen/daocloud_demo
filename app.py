from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
# redis = Redis(host='redis', port=6379)
redis = Redis(host=os.environ['REDIS_PORT_6379_TCP_ADDR'],
              port=os.environ['REDIS_PORT_6379_TCP_PORT'],
              password=os.environ.get('REDIS_PASSWORD'))


@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
