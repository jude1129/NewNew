import ollama
def ask_model_for_text(model_name, user_prompt):
    print(f"\n--- 🔵 Asking {model_name} for text ---")
    print(f"Prompt: {user_prompt[:100]}...")
    try:
        response = ollama.chat(model=model_name, messages=[{'role': 'user', 'content': user_prompt}], options={'temperature': 0.3})
        content = response['message']['content'].strip()
        print(f"🤖 Got Answer:\n{content}")
    except Exception as e:
        print(f"🚨 ERROR: {e}")

if __name__ == "__main__":
    print("\n\n*** Task 12: Function-Def GAN + Evaluation ***")
    prompt = """
    1.  First, provide Python code (using 'torch.nn') for a
        minimal GAN ('Generator' and 'Discriminator' classes)
        that could learn to generate simple Python functions.
        
    2.  Second, after the code, add '--- EVALUATION ---'.
        Explain how you would evaluate the Generator's output.
    """
    ask_model_for_text("qwen:0.5b", prompt)