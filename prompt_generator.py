import json
import random

def load_prompts():
    with open("prompts.json", "r", encoding="utf-8") as file:
        return json.load(file)

def generate_prompt(category, prompts):
    if category not in prompts:
        print(f"Category '{category}' not found.")
        return
    return random.choice(prompts[category])

def main():
    prompts = load_prompts()
    print("AI Prompt Generator\n")
    print("Available categories:")
    for cat in prompts:
        print(f"- {cat}")
    
    category = input("\nEnter a category: ").strip().lower()
    prompt = generate_prompt(category, prompts)
    
    if prompt:
        print(f"\n🎯 Prompt: {prompt}")
        save = input("Save this prompt to a file? (y/n): ").strip().lower()
        if save == 'y':
            with open("saved_prompts.txt", "a", encoding="utf-8") as f:
                f.write(prompt + "\n")
            print("Prompt saved to 'saved_prompts.txt'.")

if __name__ == "__main__":
    main()
