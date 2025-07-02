import argparse
import os
import datetime
from langchain_ollama import OllamaLLM
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv

# set OLLAMA_MODEL env var or create a .env file with OLLAMA_MODEL set to the model of your choice
load_dotenv()

ollama_model = os.getenv("OLLAMA_MODEL","qwen3:32b")

def save_to_markdown(title, content, url, filename):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    word_count = len(content["output_text"].split())
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"**Source URL:** {url}\n\n")
        f.write(f"**Timestamp:** {timestamp}\n\n")
        f.write(f"**Word Count:** {word_count}\n\n")
        f.write(f"---\n\n")
        f.write(content["output_text"])

def main():
    # setting up commandline arguments
    parser = argparse.ArgumentParser(description="Summarize a webpage via a llm model available via ollama")
    parser.add_argument("website", type=str, help="The URL of the website to summarize.")
    parser.add_argument("-o", "--output", type=str, help="Output markdown file to save the summary. If not provided, output will be printed to stdout.")
    args = parser.parse_args()

    # load into langchain
    loader = WebBaseLoader(args.website)
    docs = loader.load()

    # invoke langchain
    llm = OllamaLLM(model=ollama_model, temperature=0)
    chain = load_summarize_chain(llm, chain_type="stuff")

    result = chain.invoke(docs)

    # Extract webpage title and other metadata
    title = "Webpage Summary"  # Default title if none is found
    if docs and docs[0].metadata and "title" in docs[0].metadata:
        title = docs[0].metadata["title"]

    if args.output:
        save_to_markdown(title, result, args.website,
                        args.output)
    else:
        word_count = len(result["output_text"].split())
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"# {title}\n")
        print(f"**Source URL:** {args.website}\n")
        print(f"**Timestamp:** {timestamp}\n")
        print(f"**Word Count:** {word_count}\n")
        print(f"---\n")
        print(result)

if __name__ == "__main__":
    main()

