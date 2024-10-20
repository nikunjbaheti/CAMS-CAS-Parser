import subprocess
import os

def run_script(script_name):
    try:
        # Run the script using subprocess
        subprocess.run(['python', script_name], check=True)
        print(f"{script_name} ran successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")
        return False

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"{file_name} deleted successfully.")
    except FileNotFoundError:
        print(f"{file_name} not found.")

# Run Ashok's scripts
if run_script('Ashok CASParser.py'):
    if run_script('Ashok Cleanup.py'):
        delete_file('Ashok.csv')

# Run Nikunj's scripts
if run_script('Nikunj CASParser.py'):
    if run_script('Nikunj Cleanup.py'):
        delete_file('Nikunj.csv')

# Run Vatsal's scripts
if run_script('Vatsal CASParser.py'):
    if run_script('Vatsal Cleanup.py'):
        delete_file('Vatsal.csv')
