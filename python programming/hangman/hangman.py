import random  # to randomly choose a word

# Step 1: Define a small list of words
words = ['apple', 'chair', 'snake', 'light', 'tiger']

# Step 2: Pick one word randomly
word = random.choice(words)

# Step 3: Create a hidden version of the word, like '_ _ _ _ _'
guessed_word = ['_'] * len(word)

# Step 4: Setup guessed letters list and attempt counter
guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman!")
print("You have 6 chances to guess the word.")
print(" ".join(guessed_word))  # Show the initial blank word

# Step 5: Run the game loop
while attempts > 0 and '_' in guessed_word:
    guess = input("🔤 Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Step 6: Check if the guessed letter is in the word
    if guess in word:
        print("✅ Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")

    print(" ".join(guessed_word))  # Show updated word

# Step 7: End of game result
if '_' not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over! The word was:", word)
