# 8
class Logger:
    def log(self, event, player, filename):
        log_line = f"{event.timestamp};{player.id};{event.type};{event.data}\n"
        with open(filename, mode="a", encoding="utf-8") as file:
            file.write(log_line)

        print(f"Оқиға '{filename}' файлына сәтті жазылды.")


class MockEvent:
    def __init__(self):
        self.timestamp = "2026-04-10 15:30:00"
        self.type = "ATTACK"
        self.data = "{'damage': 15}"


class MockPlayer:
    def __init__(self):
        self.id = 101


logger = Logger()
e = MockEvent()
p = MockPlayer()

logger.log(e, p, "game_history.txt")