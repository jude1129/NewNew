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
            options={'temperature': 0.3} # Higher temp for creativity
        )
        content = response['message']['content'].strip()
        print(f"🤖 Got Answer:\n{content}")
        return content
    except Exception as e:
        print(f"🚨 ERROR: Could not talk to Ollama.\n   Is it running? Have you pulled '{model_name}'?\n   Details: {e}")
        return None

def task_q3_string_reverse():
    """
    PDF Q3: Generate a string reverse function and ask for optimization.
    """
    print("\n\n*** Task 3: (Generate + Predict) - String Reverse [PDF Q3] ***")
    model_name = "qwen:0.5b"
    prompt = """
    First, provide a Python function 'reverse_string(s)' that
    reverses a string without using slicing ([::-1]).
    
    Second, after the code, add a section named '--- OPTIMIZATION ---'.
    In that section, explain how this code can be optimized
    for faster execution.
    """
    
    # 1. Get the combined code and text from the model
    # We don't need to test, just print the model's full answer.
    ask_model_for_text(model_name, prompt)

if __name__ == "__main__":
    task_q3_string_reverse()