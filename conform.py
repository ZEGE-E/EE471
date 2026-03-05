# Senior Dev: Zeynep vol 1

def conform(value, min_val, max_val):
    """Clamps a value between min and max."""
    return max(min_val, min(max_val, value))

def main():
    print(conform(15, 0, 10))
    print(conform(-5, 0, 10))
    print(conform(7, 0, 10))

if __name__ == "__main__":
    main()