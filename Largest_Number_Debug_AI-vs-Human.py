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

def task_q7_multi():
    """
    PDF Q7: Part 1: Debug largest number. Part 2: Predict AI-gen code.
    """
    print("\n\n*** Task 7: (Debug + Predict) [PDF Q7] ***")
    
    # --- Part 1: Debug largest number (uses CodeLlama) ---
    print("\n--- Part 7a: Debugging Largest Number ---")
    model_name_1 = "codellama:7b"
    prompt_1 = """
    The following code fails for equal values (e.g., 5, 5, 5).
    
    Buggy Code:
    def find_largest(a, b, c):
        if a > b and a > c:
            return a
        elif b > a and b > c:
            return b
        else:
            return c

    Please fix the logical bug.
    Provide ONLY the complete, corrected Python code for the function.
    """
    
    fixed_code_string = ask_model_for_code(model_name_1, prompt_1)
    
    if fixed_code_string:
        print("\n--- 🟢 Testing the Model's Fixed Code ---")
        try:
            local_scope = {}
            exec(fixed_code_string, {}, local_scope)
            test_func = local_scope.get('find_largest')
            
            if test_func:
                test_input = (5, 5, 5)
                expected = 5
                result = test_func(*test_input)
                print(f"Test: find_largest{test_input} -> {result} (Expected: {expected})")
                if result == expected:
                    print("   ✅ PASSED! The bug is fixed.")
                else:
                    print("   ❌ FAILED!")
            else:
                print("❌ ERROR: I couldn't find the 'find_largest' function.")
        except Exception as e:
            print(f"❌ ERROR: The fixed code could not be run.\n   Error details: {e}")

    # --- Part 2: Predict AI vs. Human (uses Gemma) ---
    print("\n--- Part 7b: Predicting AI vs. Human Code ---")
    model_name_2 = "gemma:7b"
    prompt_2 = """
    Analyze the following Python function.
    Is it more likely to be AI-generated or human-written?
    Give a short, one-paragraph justification.

    Function to analyze:
    def check_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    """
    # This is a prediction task, so we just print the model's text answer
    ask_model_for_text(model_name_2, prompt_2)

if __name__ == "__main__":
    task_q7_multi()