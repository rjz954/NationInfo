import subprocess

# List of Python programs to run
programs = [
    "csvmerger.py",
    "csvcountrylist.py",
    "series.py",
    "init.py",
    "load_data.py",
    "app.py"
]

# Run each program in order
for program in programs:
    try:
        subprocess.run(["python", program], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {program}: {e}")
        continue
