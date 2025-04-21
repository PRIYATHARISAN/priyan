import threading
import time

text = "Multithreading is useful for concurrent execution"

def print_words():
    words = text.split()
    for word in words:
        print("Word:", word)
        time.sleep(2)

def print_vowels():
    vowels = "AEIOUaeiou"
    for char in text:
        if char in vowels:
            print("Vowel:", char)
            time.sleep(2)

# Creating threads
word_thread = threading.Thread(target=print_words)
vowel_thread = threading.Thread(target=print_vowels)

# Start threads
word_thread.start()
vowel_thread.start()

# Wait for threads to finish
word_thread.join()
vowel_thread.join()
