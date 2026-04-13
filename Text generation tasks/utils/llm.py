from huggingface_hub import InferenceClient
import os

def load_llm():
    """
    Load Hugging Face API model (FREE)
    """
    client = InferenceClient(
        provider="hf-inference",
        api_key=os.getenv("HF_TOKEN")   # set env variable
    )

    def llm(prompt):
        response = client.text_generation(
            prompt,
            model="mistralai/Mistral-7B-Instruct-v0.1",  # free model
            max_new_tokens=512,
            temperature=0.7
        )
        return response

    return llm
