# 9
class Logger:
    def read_logs(self, filename: str):
        events_list = []

        try:
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(";")
                    if len(parts) == 4:
                        t_stamp = parts[0]
                        p_id = parts[1]
                        e_type = parts[2]
                        e_data = parts[3]

                        new_event = Event(e_type, e_data)

                        new_event.timestamp = t_stamp

                        events_list.append(new_event)

        except FileNotFoundError:
            print(f"Қате: {filename} файлы табылмады!")

        return events_list


class Event:
    def __init__(self, type, data):
        self.type = type
        self.data = data
        self.timestamp = ""


logger = Logger()
history = logger.read_logs("game_logs.txt")

for e in history:
    print(f"Уақыты: {e.timestamp} | Оқиға: {e.type} | Мәлімет: {e.data}")