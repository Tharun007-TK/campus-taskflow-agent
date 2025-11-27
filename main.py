import os
import sys
import argparse
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def main():
    print(Fore.CYAN + "Welcome to Campus TaskFlow Agent")
    print(Fore.CYAN + "================================")
    
    parser = argparse.ArgumentParser(description="Campus TaskFlow Agent")
    parser.add_argument("--file", help="Path to the PDF file to process")
    args = parser.parse_args()

    if not args.file:
        print(Fore.YELLOW + "No file provided. Usage: python main.py --file <path_to_pdf>")
        # For interactive mode later
        file_path = input(Fore.GREEN + "Please enter the path to the PDF file: ").strip()
    else:
        file_path = args.file

    if not os.path.exists(file_path):
        print(Fore.RED + f"Error: File '{file_path}' not found.")
        return

    print(Fore.BLUE + f"Processing file: {file_path}")
    
    from agents.orchestrator import Orchestrator
    orchestrator = Orchestrator()
    orchestrator.process(file_path)

    print(Fore.GREEN + "Processing complete.")

if __name__ == "__main__":
    main()
