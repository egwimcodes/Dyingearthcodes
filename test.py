import random

def generate_unique_code():
    unique_id = '-'.join([''.join(random.choices('0123456789abcdefghijklmnopqrstuvwxyz', k=4)) for _ in range(4)])
    formatted_code = f"DE-{unique_id}"
    return formatted_code.upper()

# Example usage:
print(generate_unique_code())
print(len(generate_unique_code()))