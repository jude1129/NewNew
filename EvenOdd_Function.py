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
            options={'temperature': 0.0} # Low temp for code
        )
        content = response['message']['content']
        # Clean up the ```python ... ``` blocks
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

def task_q1_even_odd():
    """PDF Q1: Generate and test an even/odd function."""
    print("\n\n*** Task 1: (Generate + Test) - Even/Odd [PDF Q1] ***")
    
    model_name = "gemma:7b"
    prompt = """
    Generate a Python function 'check_even_odd(n)' that checks if a
    number is even or odd. It should return the string "Even" or "Odd".
    
    Provide ONLY the Python code for the function, and nothing else.
    """
    
    # 1. Get the code from the model as a string
    code_string = ask_model_for_code(model_name, prompt)
    
    if code_string is None:
        print("Model failed to provide code. Exiting.")
        return

    # 2. Test the code string
    print("\n--- 🟢 Testing the Model's Code ---")
    try:
        # EXPLANATION:
        # We need to run the 'code_string' the model gave us.
        # 'exec()' is Python's way of running code from a string.
        # We create an empty dictionary 'local_scope' to "catch"
        # the function 'exec()' creates.
        
        local_scope = {}
        exec(code_string, {}, local_scope)
        
        # 3. Find the function 'exec()' created
        # We look inside 'local_scope' for the function we asked for.
        test_func = local_scope.get('check_even_odd')

        if test_func:
            # 4. Run our tests on the model's function
            inputs = [2, 7, 10, 13, 0]
            expected = ["Even", "Odd", "Even", "Odd", "Even"]
            
            for num, exp in zip(inputs, expected):
                result = test_func(num)
                print(f"Test: check_even_odd({num}) -> '{result}' (Expected: '{exp}')")
                if result != exp:
                    print("   ❌ FAILED")
                else:
                    print("   ✅ PASSED")
            print("--- Test Finished ---")
            
        else:
            print("❌ ERROR: The model's code ran, but I couldn't find the 'check_even_odd' function.")

    except Exception as e:
        print(f"❌ ERROR: The code from the model could not be run.\n   Error details: {e}")

if __name__ == "__main__":
    task_q1_even_odd()