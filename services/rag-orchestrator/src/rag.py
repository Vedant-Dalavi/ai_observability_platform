from llm import ask_llm
from search import retrieve_logs

def build_prmpt(query:str, retrieved: list):
    context_text = "\n".join(
        [
            f"- ({log['service']} | {log['level']} | {log['timestamp']}): {log['message']}"
            for log in retrieved
        ]
    )

    prompt = f"""
            You are as SRE assistant. Analyze the logs and answer the question.
            
            User Query:
            {query}

            Relevant Logs:
            {context_text}

            Provide:
            - Cause summary
            - Which service is affected
            - Most likely root cause
            - Possible fix

            Give Answer in strict pure JSON format
            Answer =  
            """
    
    return prompt

def run_rag(query:str):
    print("inside run rag")
    retrieved = retrieve_logs(query)
    print("retrived logs", retrieved)
    prompt = build_prmpt(query,retrieved)
    print("prompt: ", prompt)
    answer = ask_llm(prompt)
    print("answer",answer)
    return {
        "query":query,
        "context":retrieved,
        "answer":answer
    }
