from agents.base_agent import BaseAgent

class CalendarAgent(BaseAgent):
    def __init__(self):
        super().__init__()

    def schedule_events(self, plan: list):
        """
        Mock function to schedule events.
        In a real app, this would use Google Calendar API.
        """
        print("Scheduling events to calendar...")
        for item in plan:
            print(f"  [Calendar] Scheduled: {item['action']} ({item['estimated_duration']}) for {item['suggested_day']}")
        
        return True
