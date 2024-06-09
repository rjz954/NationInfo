import subprocess


programs = [
    "csvmerger.py",
    "csvcountrylist.py",
    "series.py",
    "init.py",
    "load_data.py",
    "app.py"]


for program in programs:
    try:
        subprocess.run(["python", program], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {program}: {e}")
        continue
