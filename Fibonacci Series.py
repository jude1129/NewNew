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

def task_q6_fibonacci():
    """
    PDF Q6: Generate a Fibonacci function and modify it to
    handle invalid inputs.
    """
    print("\n\n*** Task 6: (Generate + Modify) - Fibonacci [PDF Q6] ***")
    model_name = "gemma:7b"
    prompt = """
    Generate a Python function 'fibonacci_series(n)' that
    returns a list of the Fibonacci series up to N terms.
    
    IMPORTANT: The function MUST handle invalid inputs
    (like 0 or negative numbers) by returning an empty list [].
    
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
        test_func = local_scope.get('fibonacci_series')
        
        if test_func:
            # 4. Run tests, including the invalid ones
            inputs = [5, 1, 0, -2]
            expected = [[0, 1, 1, 2, 3], [0], [], []]
            
            for num, exp in zip(inputs, expected):
                result = test_func(num)
                print(f"Test: fibonacci_series({num}) -> {result} (Expected: {exp})")
                if result != exp:
                    print("   ❌ FAILED")
                else:
                    print("   ✅ PASSED")
            print("--- Test Finished ---")
            
        else:
            print("❌ ERROR: I couldn't find the 'fibonacci_series' function.")

    except Exception as e:
        print(f"❌ ERROR: The code from the model could not be run.\n   Error details: {e}")

if __name__ == "__main__":
    task_q6_fibonacci()