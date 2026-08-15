# Step 1: Collect user information using input() and store in variables
name = input("What is your name? ")
age = input("How old are you? ")
city = input("Which city are you from? ")
hobby = input("What is your favorite hobby? ")
favorite_food = input("What is your favorite food? ")
favorite_language = input("What programming language are you excited to learn? ")

# Step 2: Display a warm, personalized welcome message
print("\n" + "=" * 40)
print(f"✨ Welcome to the Community, {name}! ✨")
print("=" * 40)
print(f"It's awesome to meet someone from {city} who is {age} years young.")
print(f"Spending time doing {hobby} sounds super fun, especially with a plate of {favorite_food}!")
print(f"We're thrilled to have you here starting your journey with {favorite_language}.")
print("Have a fantastic time learning and building great things! 🚀")