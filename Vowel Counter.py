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
            content = content.split("```python")[1].split("```")[0]
        elif "```" in content:
            content = content.split("```")[1].split("```")[0]
        content = content.strip()
        print(f"🤖 Got Code:\n{content}")
        return content
    except Exception as e:
        print(f"🚨 ERROR: Could not talk to Ollama.\n   Is it running? Have you pulled '{model_name}'?\n   Details: {e}")
        return None

def task_q4_vowel_counter():
    """PDF Q4: Generate and test a vowel counter."""
    print("\n\n*** Task 4: (Generate + Test) - Vowel Counter [PDF Q4] ***")
    
    model_name = "gemma:7b"
    prompt = """
    Generate a Python function 'count_vowels(s)' that counts the
    number of vowels (a, e, i, o, u) in a given string.
    The function must be case-insensitive.
    
    Provide ONLY the Python code for the function.
    """
    
    # 1. Get the code from the model
    code_string = ask_model_for_code(model_name, prompt)
    
    if code_string is None:
        print("Model failed to provide code. Exiting.")
        return

    # 2. Test the code
    print("\n--- 🟢 Testing the Model's Code ---")
    try:
        # Use exec() to run the model's code
        local_scope = {}
        exec(code_string, {}, local_scope)
        
        # 3. Find the function
        test_func = local_scope.get('count_vowels')

        if test_func:
            # 4. Run tests
            inputs = ["Apple", "Karunya", "University", "rhythm"]
            expected = [2, 3, 5, 0]
            
            for s, exp in zip(inputs, expected):
                result = test_func(s)
                print(f"Test: count_vowels('{s}') -> {result} (Expected: {exp})")
                if result != exp:
                    print("   ❌ FAILED")
                else:
                    print("   ✅ PASSED")
            print("--- Test Finished ---")
            
        else:
            print("❌ ERROR: I couldn't find the 'count_vowels' function.")

    except Exception as e:
        print(f"❌ ERROR: The code from the model could not be run.\n   Error details: {e}")

if __name__ == "__main__":
    task_q4_vowel_counter()