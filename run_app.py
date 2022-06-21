import os
import sys


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

path = 'app.py'
command = f'streamlit run {path}'
os.system(command)
