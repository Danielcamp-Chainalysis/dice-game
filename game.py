import random

def roll_dice():
    """Roll a single die (1-6)"""
    return random.randint(1, 6)

def roll_multiple_dice(num):
    """Roll multiple dice"""
    if num <= 0:
        return []
    return [roll_dice() for _ in range(num)]

def calculate_score(rolls):
    """Calculate total score from rolls"""
    if not rolls:
        return 0
    return sum(rolls)

def main():
    print("Welcome to Dice Game!")
    print("Rolling one die...")
    result = roll_dice()
    print(f"You rolled: {result}")
    
    # Calculate score
    score = calculate_score([result])
    print(f"Score: {score}")

if __name__ == "__main__":
    main()
