# 📚 Bloom Filter in Python using `bitarray`

A simple, fast, and space-efficient **Bloom Filter** implemented in Python for set membership testing.  
Think of it like a magical checklist that answers:

> ❓ *"Is this item probably in the set?"*  
> ✅ *Yes (maybe)*  
> ❌ *No (definitely not)*

---

## 🔍 What is a Bloom Filter?

A **Bloom Filter** is a probabilistic data structure that helps determine whether an element is **possibly in a set** or **definitely not**.

- 🚫 It **can return false positives** (thinks something is present when it's not).
- ✅ But **never false negatives** (never says missing when it’s present).

---

## 🛍️ Real-World Analogy — Bookstore Example

Imagine a large **online bookstore** with thousands of books.  
You want to check if a book 📖 is *probably* already listed before performing an expensive database lookup.

Instead of searching the full catalog:

1. You check the **Bloom Filter**.
2. If it says **"No"**, skip the lookup — it's definitely not there.
3. If it says **"Maybe"**, then do the full search.

➡️ This saves time and resources, especially with **millions of records**!

---

## 🛠️ How It Works

- Uses a **bit array** (🧠 memory-efficient).
- Applies **multiple hash functions** 🔁 to generate positions in the array.
- To add an item, it sets multiple bits to 1.
- To check an item, it sees if all bits at those positions are 1.

---

## ⚙️ Why Use Multiple Hash Functions? (`hash_count`)

- 🧠 **More hash functions = fewer false positives**, because we spread the "markings" better across the array.
- BUT 📉 **Too many hashes** = more time per insert/check and may increase false positives if overused.
- So, a balance is key!

✅ **Optimal hash count**:
\[
k = \left(\frac{m}{n}\right) \ln 2
\]

Where:
- `m` = size of bit array
- `n` = number of inserted items

---

## ⚡ Reducing False Positives

Here are ways to reduce the error rate of a Bloom Filter:

### ✅ 1. Increase the Bit Array Size (`size`)
- Larger size → fewer collisions → lower false positive rate.

### ✅ 2. Increase Number of Hash Functions (`hash_count`)
- More hash functions spread bits better, up to an optimal point.
- After that, more hashes might hurt performance or increase error.

### ✅ 3. Control the Number of Elements Added
- Don’t overflow the Bloom Filter.
- Reset or rotate if it exceeds capacity.

### ✅ 4. Use Better Hash Functions
- Use `sha256`, `sha1`, or `mmh3` (MurmurHash) for better randomness.

### 📉 Formula to Estimate False Positive Probability:

\[
P = \left(1 - e^{-\frac{k \cdot n}{m}}\right)^k
\]

Where:
- `P` = false positive rate
- `k` = number of hash functions
- `n` = number of elements added
- `m` = bit array size

---

## 📦 Requirements

- Python 3.x
- `bitarray` module

Install with:
```bash
pip install bitarray
