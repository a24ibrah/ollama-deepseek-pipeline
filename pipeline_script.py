import os
import json
from github import Github
from ollama import Ollama
import re

def extract_text(file_path, content):
    # Extract text based on file type
    if file_path.endswith((".md", ".py", ".txt", ".json")):
        return content  # Use text-based files as-is
    else:
        return None  # Skip binary or unsupported files

def clean_text(text):
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters (optional)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

def fetch_repo_data(repo_name):
    g = Github("your_github_token")
    repo = g.get_repo(repo_name)
    return repo.get_contents("")

def preprocess_and_convert(repo_name):
    files = fetch_repo_data(repo_name)
    llm_data = []
    for file in files:
        text = extract_text(file.path, file.decoded_content.decode())
        if text:
            llm_data.append({
                "path": file.path,
                "content": clean_text(text)
            })
    return llm_data

if __name__ == "__main__":
    repo_name = "owner/repo_name"
    llm_data = preprocess_and_convert(repo_name)
    
    # Save preprocessed data
    with open("llm_data.json", "w") as f:
        json.dump(llm_data, f)
    
    # Initialize Ollama with Deepseek
    ollama = Ollama(model_path="path/to/deepseek-model-weights.bin")
    
    # Process data with Ollama
    summaries = []
    for item in llm_data:
        prompt = f"Summarize the following content from {item['path']}:\n{item['content']}"
        summary = ollama.generate(prompt)
        summaries.append({
            "path": item["path"],
            "summary": summary
        })
    
    # Save summaries
    with open("summaries.json", "w") as f:
        json.dump(summaries, f)
