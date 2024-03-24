import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return f"{self.name} ({self.start_date.strftime('%d/%m/%Y')}), Priority: {self.priority}, Cost: ${self.cost_estimate:.2f}, Completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Sort projects by priority."""
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage == 100