import ollama
import sys

def ask_model_for_text(model_name, user_prompt):
    """A simple function to get a text answer from an Ollama model."""
    print(f"\n--- 🔵 Asking {model_name} ---")
    print(f"Prompt: {user_prompt[:100]}...")
    try:
        response = ollama.chat(
            model=model_name,
            messages=[{'role': 'user', 'content': user_prompt}],
            options={'temperature': 0.3}
        )
        content = response['message']['content'].strip()
        print(f"🤖 Got Answer:\n{content}")
        return content
    except Exception as e:
        print(f"🚨 ERROR: Could not talk to Ollama.\n   Is it running? Have you pulled '{model_name}'?\n   Details: {e}")
        return None

def task_q10_sum_evens():
    """
    PDF Q10: Generate code for sum of evens, and predict
    AI vs. human differences.
    """
    print("\n\n*** Task 10: (Generate + Predict) - Sum of Evens [PDF Q10] ***")
    model_name = "gemma:7b"
    prompt = """
    First, generate a Python function 'sum_evens(lst)' to
    calculate the sum of only the even numbers in a list.
    
    Second, after the code, add a section named '--- PREDICTION ---'.
    In that section, predict how an AI-generated version of this code
    might differ from a typical human-written one.
    """
    
    # 1. Get the combined code and text from the model
    # We just print the model's full answer.
    ask_model_for_text(model_name, prompt)

if __name__ == "__main__":
    task_q10_sum_evens()