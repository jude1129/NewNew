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

def task_q12_gan_functions():
    """
    PDF Q12: Build a minimal GAN to generate function definitions
    and evaluate its output.
    """
    print("\n\n*** Task 12: (Generate + Predict) - Function-Def GAN [PDF Q12] ***")
    model_name = "gemma:7b"
    prompt = """
    This is a two-part task:
    
    1.  First, provide the Python code (using 'torch.nn') for a
        minimal GAN (both 'Generator' and 'Discriminator' classes)
        that could learn to generate simple Python function
        definitions (e.g., 'def add(a, b): return a + b').
        
    2.  Second, after the code, add a section named '--- EVALUATION ---'.
        In that section, explain how you would evaluate the
        Generator's output to check if the generated functions
        look AI-generated.
    """
    
    # 1. Get the combined code and text from the model
    # We are not testing this, just printing the model's full answer.
    print("Note: This script just prints the model's answer.")
    print("It does not run or test the complex GAN structure.")
    ask_model_for_text(model_name, prompt)

if __name__ == "__main__":
    task_q12_gan_functions()