import zmq

context = zmq.Context()
s = context.socket(zmq.SUB)
p = "tcp://localhost:5555"
s.connect(p)
s.setsockopt(zmq.SUBSCRIBE, b"TIME")  # subscribe to TIME message

for i in range(10):
    time = s.recv()
    print(time)
