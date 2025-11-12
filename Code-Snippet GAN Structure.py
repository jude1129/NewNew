import ollama
import sys

def ask_model_for_code(model_name, user_prompt):
    """A simple function to get code from an Ollama model."""
    print(f"\n--- 🔵 Asking {model_name} ---")
    print(f"Prompt: {user_prompt[:100]}...")
    try:
        response = ollama.chat(
            model=model_name,
            messages=[{'role': 'user', 'content': user_prompt}],
            options={'temperature': 0.0}
        )
        content = response['message']['content']
        # This code is complex, so we are less strict with cleaning.
        if "```python" in content:
            content = content.split("```python", 1)[1].rsplit("```", 1)[0]
        content = content.strip()
        print(f"🤖 Got Code:\n{content}")
        return content
    except Exception as e:
        print(f"🚨 ERROR: Could not talk to Ollama.\n   Is it running? Have you pulled '{model_name}'?\n   Details: {e}")
        return None

def task_q11_gan_structure():
    """
    PDF Q11: Create a simple GAN structure for code snippets.
    """
    print("\n\n*** Task 11: (Generate) - Code-Snippet GAN Structure [PDF Q11] ***")
    model_name = "codellama:7b"
    prompt = """
    Generate a simple GAN structure in Python using 'torch' and 'torch.nn'.
    
    I need two classes:
    1. A 'Generator' class that takes random noise and outputs a
       (simplified) "code snippet".
    2. A 'Discriminator' class that takes a "code snippet" and
       classifies it as AI-generated (0) or human-written (1).
    
    Provide ONLY the Python code for these two classes.
    You do not need to provide the training loop or imports.
    """
    
    # 1. Get the code from the model
    # We are not testing this, just printing the generated structure.
    print("Note: This script just prints the model's generated code.")
    print("It does not run or test the complex GAN structure.")
    ask_model_for_code(model_name, prompt)

if __name__ == "__main__":
    task_q11_gan_structure()