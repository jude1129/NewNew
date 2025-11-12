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
        if "```python" in content:
            content = content.split("```python", 1)[1].rsplit("```", 1)[0]
        content = content.strip()
        print(f"🤖 Got Code:\n{content}")
        return content
    except Exception as e:
        print(f"🚨 ERROR: Could not talk to Ollama.\n   Is it running? Have you pulled '{model_name}'?\n   Details: {e}")
        return None

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

def task_q13_gan_prototype():
    """
    PDF Q13: Combine Qwen (Generator) and Gemma (Discriminator)
    and explain the discriminator.
    """
    print("\n\n*** Task 13: (Generate + Predict) - GAN Prototype [PDF Q13] ***")
    print("Note: This script just prints the models' answers.")
    
    # --- Part 1: Qwen as Generator ---
    print("\n--- Part 13a: Qwen as Generator ---")
    model_name_qwen = "qwen:0.5b"
    prompt_gen = """
    Design a prototype 'Generator' class for a GAN in Python
    using 'torch.nn'.
    This Generator will be used to generate code snippets.
    It should take a latent vector (noise) as input.
    
    Provide ONLY the Python code for the 'Generator' class.
    """
    ask_model_for_code(model_name_qwen, prompt_gen)

    # --- Part 2: Gemma as Discriminator and Explainer ---
    print("\n--- Part 13b: Gemma as Discriminator and Explainer ---")
    model_name_gemma = "gemma:7b"
    prompt_disc = """
    A 'Generator' model creates fake code snippets.
    
    1.  First, provide the Python code (using 'torch.nn') for a
        'Discriminator' model. This model will take a
        code snippet and classify it as real (1) or fake (0).
        
    2.  Second, after the code, add a section named '--- EXPLANATION ---'.
        In that section, explain clearly how this
        Discriminator model improves during GAN training.
    """
    ask_model_for_text(model_name_gemma, prompt_disc)

if __name__ == "__main__":
    task_q13_gan_prototype()