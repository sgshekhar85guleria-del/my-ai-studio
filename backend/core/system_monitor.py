import datetime


class SystemMonitor:

    def __init__(self):
        self.logs = []

    def log(self, message):
        entry = {
            "time": str(datetime.datetime.now()),
            "message": message
        }
        self.logs.append(entry)
        print("[SYSTEM LOG]", entry)

    def get_logs(self):
        return self.logs