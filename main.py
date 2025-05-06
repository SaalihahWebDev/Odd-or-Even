import random

print("🎯 Let's find the ODD number!")
print("Odd numbers end in 1, 3, 5, 7, or 9.")

# Show 5 randow numbers
numbers = random.sample(range(1, 100), 5)

print("\nLook at these number:")
for num in numbers:
    print(num)

# Ask one by one: Is this number odd?
score = 0
for num in numbers:
    answer = input(f"\nIs {num} an odd number? (yes or no): ").lower()
    if (num % 2 == 1 and answer == "yes") or (num % 2 == 0 and answer == "no"):
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Oops! That's not right.")
        if num % 2 == 1:
            print(f"{num} is ODD.")
        else:
            print(f"{num} is EVEN.")
        
print(f"\n All done! You got {score} out of 5 corrent.")