# Ollama Web Summarizer

A Python script that uses Ollama's local LLMs to summarize web pages via LangChain.

## First Run Setup

1. Install Ollama (if not already installed):
```bash
brew install ollama
```

2. Download a model (e.g., llama3):
```bash
ollama pull llama3
```

3. Create and activate a Python virtual environment:
```bash
python -m venv venv

# For bash/zsh:
source venv/bin/activate

# For fish shell:
source venv/bin/activate.fish

4. Install dependencies:
```bash
uv pip install -r requirements.txt
```

5. Create a .env file to specify your model:
```bash
echo "OLLAMA_MODEL=llama3" > .env
```

## Usage

To summarize a webpage and save to a markdown file:
```bash
python summarize.py https://example.com -o summary.md
```

To print summary to console:
```bash
python summarize.py https://example.com
```

## Configuration

- Edit `.env` to change the default model
- Supported models: Any model available in Ollama (run `ollama list` to see installed models)

## Troubleshooting

If you get connection errors:
- Make sure Ollama is running: `ollama serve`
- Check model name is correct in `.env`
