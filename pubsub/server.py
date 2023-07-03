import zmq, time


if __name__ == "__main__":
    context = zmq.Context()
    s = context.socket(zmq.PUB)
    p = "tcp://*:5555"
    s.bind(p)
    while True:
        time.sleep(1)
        s.send_string("TIME " + time.asctime())
