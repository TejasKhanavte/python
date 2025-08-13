
borrow_records = {
    'Alice': 3,
    'Bob': 0,
    'Charlie': 5,
    'David': 2,
    'Eve': 0,
    'Frank': 5,
    'Grace': 1
}


def compute_average(records):
    total = sum(records.values())
    count = len(records)
    return total / count


def find_max_min(records):
    non_zero_values = [val for val in records.values() if val > 0]
    max_borrow = max(records.values())         
    min_borrow = min(non_zero_values)          
    return max_borrow, min_borrow


def count_zero_borrowers(records):
    return list(records.values()).count(0)


def find_mode(records):
    from collections import Counter
    non_zero_values = [val for val in records.values() if val > 0]
    freq = Counter(non_zero_values)
    most_common = freq.most_common(1)[0][0]
    return most_common


average = compute_average(borrow_records)
max_borrow, min_borrow = find_max_min(borrow_records)
zero_count = count_zero_borrowers(borrow_records)
mode_borrow = find_mode(borrow_records)

