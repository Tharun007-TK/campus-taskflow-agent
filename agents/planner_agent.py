from agents.base_agent import BaseAgent
import json

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__()

    def create_plan(self, tasks: list) -> list:
        """
        Generates a study plan based on extracted tasks.
        """
        print("Generating study plan...")
        
        tasks_json = json.dumps(tasks, indent=2)
        
        prompt = f"""
        You are an expert academic planner. Based on the following tasks, create a study schedule.
        Break down large assignments into smaller sub-tasks.
        Suggest specific study blocks.
        
        Tasks:
        {tasks_json}
        
        Return the plan as a JSON list of objects, where each object has:
        - 'action': What to do (e.g., "Read Chapter 1", "Draft Outline")
        - 'related_task': Title of the original task
        - 'estimated_duration': e.g., "45 mins"
        - 'suggested_day': Relative day (e.g., "Day 1", "Day 2")
        
        Output JSON only.
        """
        
        response_text = self.generate_response(prompt)
        response_text = response_text.replace("```json", "").replace("```", "").strip()
        
        try:
            plan = json.loads(response_text)
            return plan
        except json.JSONDecodeError:
            print("Failed to parse plan JSON.")
            return []
