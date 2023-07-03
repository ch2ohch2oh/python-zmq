import zmq
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    context = zmq.Context()
    s = context.socket(zmq.SUB)
    p = "tcp://localhost:5555"
    s.connect(p)
    s.setsockopt(zmq.SUBSCRIBE, b"TIME")  # subscribe to TIME message

    for i in range(10):
        time = s.recv()
        print(args.name + " " + time.decode())
