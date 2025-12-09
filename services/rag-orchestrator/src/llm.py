import requests
import traceback

LLM_URL = "http://localhost:11434/api/generate" 
MODEL = "llama3"

def ask_llm(prompt: str) -> str:
    try:
        res = requests.post(
            LLM_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
            }
        )

        res.raise_for_status()
        data = res.json()  
        return data["response"]
    except Exception as e:
        traceback.print_exc()
        print("error in llm cal", e)
        