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

def task_q8_custom_sort():
    """
    PDF Q8: Generate a custom sort function and test it.
    """
    print("\n\n*** Task 8: (Generate + Test) - Custom Sort [PDF Q8] ***")
    model_name = "qwen:0.5b"
    prompt = """
    Generate a Python function 'custom_sort(lst)' to sort a
    list of numbers in ascending order.
    
    You MUST NOT use the built-in .sort() or sorted() functions.
    Use an algorithm like bubble sort or insertion sort.
    
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
        test_func = local_scope.get('custom_sort')
        
        if test_func:
            # 4. Run tests
            test_list = [5, -2, 8, 0, -10, 3]
            expected = [-10, -2, 0, 3, 5, 8]
            print(f"Testing with list: {test_list}")
            
            # Note: The model's function might sort "in-place" (modify
            # the list) or return a new list. This code handles both.
            list_copy = test_list.copy()
            result = test_func(list_copy)
            
            if result is None: # Function sorted in-place
                result = list_copy
            
            print(f"Test: custom_sort() -> {result} (Expected: {expected})")
            if result == expected:
                print("   ✅ PASSED!")
            else:
                print("   ❌ FAILED!")
            print("--- Test Finished ---")
            
        else:
            print("❌ ERROR: I couldn't find the 'custom_sort' function.")

    except Exception as e:
        print(f"❌ ERROR: The code from the model could not be run.\n   Error details: {e}")

if __name__ == "__main__":
    task_q8_custom_sort()