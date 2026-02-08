items = {
    "Avengers": ["action", "superhero", "marvel"],
    "Titanic": ["romance", "drama"],
    "Inception": ["action", "thriller", "sci-fi"],
    "The Hangover": ["comedy"],
    "Interstellar": ["sci-fi", "drama"],
    "Joker": ["drama", "thriller"]
}

print("🎬 Intelligent Recommendation System")
print("Enter interests separated by commas")
print("Example: action, sci-fi, drama\n")

user_input = input("Your interests: ").lower()
user_interests = [i.strip() for i in user_input.split(",")]

scores = {}

for item, features in items.items():
    match_count = 0
    for interest in user_interests:
        if interest in features:
            match_count += 1
    if match_count > 0:
        scores[item] = match_count

if scores:
    print("\nRecommended for you (ranked):")
    for item in sorted(scores, key=scores.get, reverse=True):
        print(f"- {item} (match score: {scores[item]})")
else:
    print("\nNo matching items found. Try different interests.")
