# Senior Dev: Zeynep

def conform(value, min_val, max_val):
    """Clamps a value between min and max."""
    return max(min_val, min(max_val, value))

def main():
    print(conform(15, 0, 10))
    print(conform(-5, 0, 10))
    print(conform(7, 0, 10))

if __name__ == "__main__":
    main()

    def pleaseConformOnepass(data, min_val, max_val):
    """Conforms all values in a single pass."""
    return [max(min_val, min(max_val, x)) for x in data if x is not None]
