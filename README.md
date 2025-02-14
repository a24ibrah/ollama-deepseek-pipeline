# GitHub Repository to Local LLM Pipeline

## Overview
This project provides a Python pipeline to automatically fetch, preprocess, and convert GitHub repositories into LLM-friendly text using **Ollama** and **Deepseek**. The pipeline allows users to process repository data locally while ensuring privacy, control, and cost-effectiveness.

## Features
- Fetches GitHub repository data using **PyGithub**.
- Preprocesses and extracts relevant text from repository files.
- Cleans and normalizes text for better LLM processing.
- Converts extracted text into JSON or plain text formats.
- Uses **Ollama** and **Deepseek** to generate summaries and documentation.
- Automates the pipeline execution for continuous processing.

## Minimum Hardware Requirements
### **Minimum Configuration:**
- **CPU:** 8-core processor (Intel i7 / AMD Ryzen 7 or equivalent)
- **RAM:** 16 GB (for small-scale models and light processing)
- **GPU:** Optional (Integrated GPU or entry-level dedicated GPU)
- **Storage:** 50 GB free SSD space
- **Operating System:** Linux (Ubuntu 20.04+) or Windows 10/11 (WSL recommended)

### **Recommended Configuration:**
- **CPU:** 16-core processor (Intel i9 / AMD Ryzen 9 or Apple M1/M2)
- **RAM:** 32 GB or more
- **GPU:** NVIDIA RTX 3060 or higher
- **Storage:** 100+ GB SSD (fast NVMe preferred)
- **Operating System:** Linux (Ubuntu 22.04 recommended) or macOS

## Installation
### **Step 1: Clone the Repository**
```bash
git clone https://github.com/yourusername/github-llm-pipeline.git
cd github-llm-pipeline
```

### **Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 3: Setup Ollama & Deepseek**
1. Install Ollama from its [GitHub repository](https://github.com/ollama/ollama).
2. Download Deepseek model weights:
   ```bash
   wget https://example.com/deepseek-model-weights.bin
   ```
3. Load the model:
   ```python
   from ollama import Ollama
   ollama = Ollama(model_path="path/to/deepseek-model-weights.bin")
   ```

## Usage
### **Fetching & Processing a Repository**
Run the script with the target repository:
```bash
python pipeline_script.py
```
This will fetch and process the repository data, saving:
- Preprocessed data as `llm_data.json`
- Summaries as `summaries.json`

### **Automating the Pipeline with GitHub Actions**
You can automate this pipeline using GitHub Actions with a scheduled workflow:
```yaml
name: LLM Data Pipeline
on:
  schedule:
    - cron: '0 0 * * *'  # Run daily
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install PyGithub
      - name: Run pipeline
        run: python pipeline_script.py
```

## Contributions
Feel free to contribute by submitting PRs or issues. Improvements in text preprocessing, additional LLM integrations, or optimized performance are welcome!

## License
MIT License. See `LICENSE` for details.
