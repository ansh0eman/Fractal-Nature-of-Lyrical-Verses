import pandas as pd
import re
import string

def preprocess_text(file_path):
    def clean_text(text):
        # Remove excess white space, punctuation, and convert to lower case
        text = text.lower().strip()
        text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
        return text

    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    data = []
    work_title = ''
    subdiv_title = ''
    
    for line in lines:
        line = line.strip()
        if line.startswith('==') and line.endswith('=='):
            work_title = clean_text(line[2:-2].strip())
        elif line.startswith('[') and line.endswith(']'):
            subdiv_title = clean_text(line[1:-1].strip())
        elif line:
            clean_line = clean_text(line)
            data.append((work_title, subdiv_title, clean_line))
    
    df = pd.DataFrame(data, columns=['Work Title', 'Subdivision Title', 'Line'])
    return df