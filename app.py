# Career Path Recommender

text = input("Enter your skills: ").lower()

if "python" in text and "machine learning" in text:
    print("Best Career: ML Engineer")

elif "python" in text and "sql" in text:
    print("Best Career: Data Analyst")

elif "docker" in text or "linux" in text:
    print("Best Career: DevOps Engineer")

elif "html" in text or "javascript" in text:
    print("Best Career: Web Developer")

else:
    print("Career not found. Learn more skills!")
