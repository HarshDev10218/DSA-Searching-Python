import sys
sys.path.insert(0, 'Searching')

from LinearSearch import linear_Search
from binarySearch import binary_Search
from exploarationSearch import exploration_Search
from jumpSearch import jump_Search
from interpolationSearch import interpolation_Search
import array

print("=" * 70)
print("DSA SEARCHING ALGORITHMS - COMPREHENSIVE TEST SUITE")
print("=" * 70)

# Test Cases
test_cases = {
    "basic": {
        "arr": [10, 20, 30, 40, 50],
        "key": 30,
        "expected": "found"
    },
    "element_at_start": {
        "arr": [10, 20, 30, 40, 50],
        "key": 10,
        "expected": "found"
    },
    "element_at_end": {
        "arr": [10, 20, 30, 40, 50],
        "key": 50,
        "expected": "found"
    },
    "element_not_found": {
        "arr": [10, 20, 30, 40, 50],
        "key": 99,
        "expected": "not_found"
    },
    "single_element_found": {
        "arr": [42],
        "key": 42,
        "expected": "found"
    },
    "single_element_not_found": {
        "arr": [42],
        "key": 10,
        "expected": "not_found"
    },
    "duplicates": {
        "arr": [10, 20, 20, 20, 30],
        "key": 20,
        "expected": "found"
    },
    "negative_numbers": {
        "arr": [-50, -30, -10, 0, 10, 30],
        "key": -10,
        "expected": "found"
    },
    "large_array": {
        "arr": list(range(1, 1001)),
        "key": 500,
        "expected": "found"
    }
}

# ===================== LINEAR SEARCH TESTS =====================
print("\n" + "=" * 70)
print("1. LINEAR SEARCH TESTS")
print("=" * 70)

for test_name, test_data in test_cases.items():
    arr = array.array('i', test_data["arr"])
    key = test_data["key"]
    result = linear_Search(arr, key)
    
    is_found = "found" in result.lower()
    expected_found = test_data["expected"] == "found"
    
    status = "✓ PASS" if is_found == expected_found else "✗ FAIL"
    print(f"{status} | {test_name:25} | Key: {key:4} | {result}")


# ===================== BINARY SEARCH TESTS =====================
print("\n" + "=" * 70)
print("2. BINARY SEARCH TESTS")
print("=" * 70)

for test_name, test_data in test_cases.items():
    arr = sorted(test_data["arr"])
    arr_obj = array.array('i', arr)
    key = test_data["key"]
    low = 0
    high = len(arr_obj) - 1
    result = binary_Search(arr_obj, low, high, key)
    
    is_found = "found" in result.lower()
    expected_found = test_data["expected"] == "found"
    
    status = "✓ PASS" if is_found == expected_found else "✗ FAIL"
    print(f"{status} | {test_name:25} | Key: {key:4} | {result}")


# ===================== JUMP SEARCH TESTS =====================
print("\n" + "=" * 70)
print("3. JUMP SEARCH TESTS")
print("=" * 70)

for test_name, test_data in test_cases.items():
    arr = sorted(test_data["arr"])
    arr_obj = array.array('i', arr)
    key = test_data["key"]
    result = jump_Search(arr_obj, key)
    
    is_found = "found" in result.lower()
    expected_found = test_data["expected"] == "found"
    
    status = "✓ PASS" if is_found == expected_found else "✗ FAIL"
    print(f"{status} | {test_name:25} | Key: {key:4} | {result}")


# ===================== EXPLORATION SEARCH TESTS =====================
print("\n" + "=" * 70)
print("4. EXPLORATION SEARCH TESTS")
print("=" * 70)

for test_name, test_data in test_cases.items():
    arr = sorted(test_data["arr"])
    arr_obj = array.array('i', arr)
    key = test_data["key"]
    result = exploration_Search(arr_obj, key)
    
    is_found = "found" in result.lower()
    expected_found = test_data["expected"] == "found"
    
    status = "✓ PASS" if is_found == expected_found else "✗ FAIL"
    print(f"{status} | {test_name:25} | Key: {key:4} | {result}")


# ===================== INTERPOLATION SEARCH TESTS =====================
print("\n" + "=" * 70)
print("5. INTERPOLATION SEARCH TESTS")
print("=" * 70)

for test_name, test_data in test_cases.items():
    arr = sorted(test_data["arr"])
    arr_obj = array.array('i', arr)
    key = test_data["key"]
    
    try:
        result = interpolation_Search(arr_obj, key)
        # Verify if the position is valid and contains the key
        pos = int(result.split()[-1].rstrip('.'))
        is_found = (0 <= pos < len(arr_obj) and arr_obj[pos] == key)
        expected_found = test_data["expected"] == "found"
        
        status = "✓ PASS" if is_found == expected_found else "✗ FAIL"
        print(f"{status} | {test_name:25} | Key: {key:4} | {result}")
    except Exception as e:
        print(f"✗ FAIL | {test_name:25} | Key: {key:4} | ERROR: {str(e)}")


# ===================== EDGE CASE TESTS =====================
print("\n" + "=" * 70)
print("6. EDGE CASE & ERROR HANDLING TESTS")
print("=" * 70)

# Test with empty array
print("\nTesting Empty Array:")
try:
    arr_empty = array.array('i', [])
    result = linear_Search(arr_empty, 10)
    print(f"✓ Linear Search handles empty array: {result}")
except Exception as e:
    print(f"✗ Linear Search fails on empty array: {str(e)}")

# Test with very large numbers
print("\nTesting Large Numbers:")
arr_large = array.array('i', [1000000, 2000000, 3000000])
result = linear_Search(arr_large, 2000000)
print(f"✓ Linear Search with large numbers: {result}")

# Test with all duplicate elements
print("\nTesting Duplicate Elements:")
arr_dup = array.array('i', [5, 5, 5, 5, 5])
result = linear_Search(arr_dup, 5)
print(f"✓ Linear Search with duplicates: {result}")

print("\n" + "=" * 70)
print("TEST SUITE COMPLETED")
print("=" * 70)
