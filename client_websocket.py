import time
from websockets.sync.client import connect

duration = 5

def hello():
    with connect("ws://localhost:8080") as websocket:
        start_time = time.time()

        n_round = 0

        while True:

            websocket.send('hi')
            message = websocket.recv()
            n_round += 1

            if time.time() - start_time > duration:
                break
    print(f"Rate: {n_round/duration/2} round trips per second.")

hello()