# 2. Generate pattern N = 5
def generate_pattern(n):
    pattern = []
    for i in range(n):
        line = ''.join('=' if i == j else '+' for j in range(n))
        pattern.append(line)
    return '\n'.join(pattern)

# Example usage
print(generate_pattern(5))


