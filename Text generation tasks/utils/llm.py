from langchain_community.llms import Ollama

def load_llm():
    """
    Load local LLM using Ollama
    Make sure you installed Ollama and pulled a model
    Example: ollama run llama3
    """
    llm = Ollama(
        model="llama3",   # change to mistral / phi / gemma if needed
        temperature=0.7
    )
    return llm