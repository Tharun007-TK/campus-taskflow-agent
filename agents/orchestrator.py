from agents.pdf_agent import PDFAgent
from agents.planner_agent import PlannerAgent
from agents.calendar_agent import CalendarAgent
from agents.notes_agent import NotesAgent
from memory.memory_store import MemoryStore
from colorama import Fore

class Orchestrator:
    def __init__(self):
        self.pdf_agent = PDFAgent()
        self.planner_agent = PlannerAgent()
        self.calendar_agent = CalendarAgent()
        self.notes_agent = NotesAgent()
        self.memory = MemoryStore()

    def process(self, file_path: str):
        print(Fore.MAGENTA + "\n[Orchestrator] Starting workflow...")
        
        # 1. Extract Tasks
        print(Fore.MAGENTA + "[Orchestrator] Step 1: Extracting tasks from PDF...")
        tasks = self.pdf_agent.extract_tasks(file_path)
        if not tasks:
            print(Fore.RED + "No tasks extracted. Aborting.")
            return

        print(Fore.GREEN + f"Found {len(tasks)} tasks.")
        for t in tasks:
            print(f" - {t.get('title')} ({t.get('deadline')})")

        # 2. Plan
        print(Fore.MAGENTA + "\n[Orchestrator] Step 2: Generating study plan...")
        plan = self.planner_agent.create_plan(tasks)
        print(Fore.GREEN + "Plan generated.")
        
        # 3. Schedule
        print(Fore.MAGENTA + "\n[Orchestrator] Step 3: Scheduling events...")
        self.calendar_agent.schedule_events(plan)
        
        # 4. Summarize
        print(Fore.MAGENTA + "\n[Orchestrator] Step 4: Generating summary and flashcards...")
        summary = self.notes_agent.summarize_content(file_path)
        print(Fore.CYAN + "\nSummary:\n" + summary)
        
        flashcards = self.notes_agent.create_flashcards(file_path)
        print(Fore.CYAN + f"\nGenerated {len(flashcards)} flashcards.")

        print(Fore.MAGENTA + "\n[Orchestrator] Workflow complete.")

    def process_and_return(self, file_path: str) -> dict:
        """
        Runs the workflow and returns the results as a dictionary.
        """
        results = {}
        
        # 1. Extract Tasks
        tasks = self.pdf_agent.extract_tasks(file_path)
        results['tasks'] = tasks
        
        if not tasks:
            return results

        # 2. Plan
        plan = self.planner_agent.create_plan(tasks)
        results['plan'] = plan
        
        # 3. Schedule
        # In a real app, we might return the calendar link or status
        self.calendar_agent.schedule_events(plan)
        results['calendar_status'] = "Events scheduled (Mock)"
        
        # 4. Summarize
        summary = self.notes_agent.summarize_content(file_path)
        results['summary'] = summary
        
        flashcards = self.notes_agent.create_flashcards(file_path)
        results['flashcards'] = flashcards
        
        return results
