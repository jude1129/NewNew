import ollama
import sys

def ask_model_for_code(model_name, user_prompt):
    """A simple function to get code from an Ollama model."""
    print(f"\n--- Asking {model_name} ---")
    print(f"Prompt: {user_prompt[:100]}...")
    try:
        response = ollama.chat(
            model=model_name,
            messages=[{'role': 'user', 'content': user_prompt}],
            options={'temperature': 0.0}
        )
        content = response['message']['content']
        # Clean up the ```python ... ``` blocks
        if "```python" in content:
            content = content.split("```python")[1].split("```")[0]
        elif "```" in content:
            content = content.split("```")[1].split("```")[0]
        content = content.strip()
        print(f"Got Code:\n{content}")
        return content
    except Exception as e:
        print(f"ERROR: Could not talk to Ollama.\n   Is it running? Have you pulled '{model_name}'?\n   Details: {e}")
        return None

def task_q1_even_odd():
    """PDF Q1: Generate and test an even/odd function."""
    print("\n\n*** Task 1 (COMPLETE): (Generate + Test) - Even/Odd [PDF Q1] ***")
    
    model_name = "qwen:0.5b"
    prompt = """
    Generate a Python function 'check_even_odd(n)' that checks if a
    number is even or odd. It should return the string "Even" or "Odd".
    
    Provide ONLY the Python code for the function, and nothing else.
    """
    
    # 1. Get the code from the model
    code_string = ask_model_for_code(model_name, prompt)
    
    if code_string is None:
        print("Model failed to provide code. Exiting.")
        return

    # 2. This part runs the "Test" task
    print("\n--- Testing the Model's Code ---")
    try:
        # This part runs the code the AI gave us
        local_scope = {}
        exec(code_string, {}, local_scope)
        
        # This part finds the function the AI made
        test_func = local_scope.get('check_even_odd')

        if test_func:
            # This part runs the tests from the PDF
            inputs = [2, 7, 10, 13, 0]
            expected = ["Even", "Odd", "Even", "Odd", "Even"]
            
            for num, exp in zip(inputs, expected):
                result = test_func(num)
                print(f"Test: check_even_odd({num}) -> '{result}' (Expected: '{exp}')")
                if result != exp:
                    print("FAILED")
                else:
                    print("PASSED")
            print("--- Test Finished ---")
            
        else:
            print("ERROR: The model's code ran, but I couldn't find the 'check_even_odd' function.")

    except Exception as e:
        print(f"ERROR: The code from the model could not be run.\n   Error details: {e}")

if __name__ == "__main__":
    task_q1_even_odd()