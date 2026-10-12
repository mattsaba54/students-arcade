import random

AUTHOR = "Matthew Sabadac"
APP_NAME = "Random Motivational Message"


def run():
    messages = [
        "Believe in yourself and keep going!",
        "Every step forward is progress.",
        "You are capable of more than you think.",
        "Stay focused and never give up.",
        "Success starts with the decision to try.",
        "Keep working hard. Your effort will pay off.",
        "Small progress is still progress.",
        "Challenges are opportunities to grow."
    ]

    message = random.choice(messages)

    return f"Motivational Message: {message}"


if __name__ == "__main__":
    print(run())
