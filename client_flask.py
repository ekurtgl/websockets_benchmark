import socketio
import time

client1 = socketio.Client()
client1.connect('http://localhost:8000')

duration = 5  # sec

start_time = time.time()

n_round = 0

while True:

    data = client1.send('hi')
    n_round += 1

    if time.time() - start_time > duration:
        break

client1.disconnect()
# client2.disconnect()

print(f"Rate: {n_round/duration/2} round trips per second.")

