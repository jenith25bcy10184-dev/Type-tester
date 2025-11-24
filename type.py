import time
import random

def get_sentence():
    sentences = [

        "The quick brown fox jumps over the lazy dog.",
        "Learning Python is a fantastic way to start your engineering journey.",
        "Programming isn't just about writing code; it is about solving problems.",
        "Artificial Intelligence is rapidly changing how we interact with the world.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "Debugging is like being the detective in a crime movie where you are also the murderer.",
        "The best way to predict the future is to create it.",
        "Consistency is the key to mastering any new skill, especially coding.",
        "Always write clean code, because you never know who will read it later.",
        "Technology is best when it brings people together."
    
    ]
    return random.choice(sentences)

def calculate_wpm(time_taken, typed_text):
    # Standard formula: (number of characters / 5) / (time in minutes)
    num_chars = len(typed_text)
    wpm = (num_chars / 5) / (time_taken / 60)
    return round(wpm, 2)

def calculate_accuracy(original, typed):
    count = 0
    # Compare characters one by one up to the length of the shorter string
    min_len = min(len(original), len(typed))
    
    for i in range(min_len):
        if original[i] == typed[i]:
            count += 1
            
    accuracy = (count / len(original)) * 100
    return round(accuracy, 2)

def run_test():
    print("--- PYTHON TYPING SPEED TESTER ---")
    target_text = get_sentence()
    
    print("\nType the following sentence accurately:")
    print(f"Reference: '{target_text}'")
    
    input("\nPress ENTER to start...")
    
    start_time = time.time()
    user_input = input("Type here: ")
    end_time = time.time()
    
    time_taken = end_time - start_time
    wpm = calculate_wpm(time_taken, user_input)
    accuracy = calculate_accuracy(target_text, user_input)
    
    print("\n--- RESULTS ---")
    print(f"Time Taken: {round(time_taken, 2)} seconds")
    print(f"Typing Speed: {wpm} WPM")
    print(f"Accuracy: {accuracy}%")

if __name__ == "__main__":
    run_test()
