from itertools import count
from queue import Empty, Queue

queue = Queue()
request_ids = count(1)  


def generate_request():
    new_request = f"request_{next(request_ids)}"
    queue.put(new_request)
    print(f"Generated request: {new_request}")


def process_request():
    try:
        request = queue.get_nowait()
    except Empty:
        print("Queue is empty")
    else:
        print(f"Processing request: {request}")


def show_queue():
    print(list(queue.queue))


def main():
    while True:
        generate_request()
        process_request()

        if input("Enter — продовжити, q — вийти: ").strip().lower() == "q":
            break


# код, що більш наглядно показує, як працює черга, бо якщо
# робити за псевдокодом, то черга одразу додається і очищається.
# Варіант з псевдокоду реалізований за замовчуванням.
def interactive_main():
    commands = {
        "request": generate_request,
        "process": process_request,
        "show queue": show_queue,
    }

    while True:
        command = (
            input("Команда (request / process / show queue / q): ").strip().lower()
        )

        if command == "q":
            break

        handler = commands.get(command)
        if handler is None:
            print(
                "Невідома команда. Доступні команди: request, process, show queue, q."
            )
            continue

        handler()


if __name__ == "__main__":
    main()
