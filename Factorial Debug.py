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

def task_q2_factorial_debug():
    """PDF Q2: Debug a factorial function."""
    print("\n\n*** Task 2: (Debug) - Factorial Bug [PDF Q2] ***")
    model_name = "codellama:7b"
    prompt = """
    The following Python code fails with an infinite loop when n=0.
    
    Buggy Code:
    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)

    Please fix the bug.
    Provide ONLY the complete, corrected Python code for the function.
    """
    
    # 1. Get the *fixed* code from the model
    fixed_code_string = ask_model_for_code(model_name, prompt)
    
    if fixed_code_string is None:
        print("Model failed to provide code. Exiting.")
        return

    # 2. Test the *fixed* code
    print("\n--- 🟢 Testing the Model's Fixed Code ---")
    try:
        # We use exec() again to run the model's fixed code
        local_scope = {}
        exec(fixed_code_string, {}, local_scope)
        
        # 3. Find the 'factorial' function
        test_func = local_scope.get('factorial')
        
        if test_func:
            # 4. Run the test that was failing
            test_input = 0
            expected = 1
            result = test_func(test_input)
            
            print(f"Test: factorial({test_input}) -> {result} (Expected: {expected})")
            if result == expected:
                print("   ✅ PASSED! The bug is fixed.")
            else:
                print(f"   ❌ FAILED! Expected {expected} but got {result}.")
            print("--- Test Finished ---")
            
        else:
            print("❌ ERROR: I couldn't find the 'factorial' function in the model's fix.")

    except Exception as e:
        print(f"❌ ERROR: The fixed code from the model could not be run.\n   Error details: {e}")

if __name__ == "__main__":
    task_q2_factorial_debug()