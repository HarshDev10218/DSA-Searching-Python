# Python Search Algorithms Collection

A collection of 5 fundamental search algorithms implemented in Python using the `array` module. This repository demonstrates how different searching techniques handle data arrays, along with their respective time and space complexities.

## 🚀 Algorithms Included

1. **Linear Search** (`LinearSearch.py`)
2. **Binary Search** (`binarySearch.py`)
3. **Exploration (Exponential) Search** (`exploarationSearch.py`)
4. **Jump Search** (`jumpSearch.py`)
5. **Interpolation Search** (`interpolationSearch.py`)

---

## 📊 Complexity Analysis

| Algorithm | Best Case | Average/Worst Case | Space Complexity | Prerequisites |
| :--- | :--- | :--- | :--- | :--- |
| **Linear Search** | $O(1)$ | $O(n)$ | $O(1)$ | None (Works on unsorted arrays) |
| **Binary Search** | $O(1)$ | $O(\log n)$ | $O(1)$ | Sorted Array |
| **Exploration Search** | $O(1)$ | $O(\log n)$ | $O(\log n)$ (due to recursion) | Sorted Array |
| **Jump Search** | $O(1)$ | $O(\sqrt{n})$ | $O(1)$ | Sorted Array |
| **Interpolation Search**| $O(1)$ | $O(\log(\log n))$ | $O(1)$ | Sorted & Uniformly Distributed Array |

---

## 🛠️ Detailed Breakdown

### 1. Linear Search
* **File:** `LinearSearch.py`
* **How it works:** Sequentially checks each element of the array from the beginning until a match is found or the end of the array is reached.
* **Best used for:** Small or unsorted datasets.

### 2. Binary Search
* **File:** `binarySearch.py`
* **How it works:** A divide-and-conquer algorithm. It repeatedly divides the search interval in half. If the key value is less than the item in the middle of the interval, it narrows the interval to the lower half, and vice versa.
* **Note:** This script automatically sorts your inputs before performing the search.

### 3. Exploration (Exponential) Search
* **File:** `exploarationSearch.py`
* **How it works:** Finds a range where the key element may reside by increasing the index exponentially ($i = i \times 2$). Once the range is narrowed down, it runs a standard Binary Search within that range.
* **Best used for:** Unbounded or infinite arrays.

### 4. Jump Search
* **File:** `jumpSearch.py`
* **How it works:** Like Binary Search, it works only on sorted arrays. It checks fewer elements by stepping (or jumping) ahead by fixed steps of $\lfloor\sqrt{n}\rfloor$ instead of searching sequentially. Once it overshoots the key, it performs a backward linear search.

### 5. Interpolation Search
* **File:** `interpolationSearch.py`
* **How it works:** An improvement over Binary Search for instances where the values in a sorted array are **uniformly distributed**. Instead of always checking the middle element, it estimates the position of the key using a probing formula based on the numerical value of the key.

---

## 💻 How to Run

Make sure you have Python 3.x installed. Run any script directly from your terminal:

```bash
python LinearSearch.py
