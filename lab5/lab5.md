```md
# PART B: Big-O Analysis

**n = the number of nodes in the linked list**

---

## 1. `__init__(self)`

**T(n):** 1  
**O(1)**

**Reason:** It only sets the head to None.

---

## 2. `is_empty(self)`

**T(n):** 1  
**O(1)**

**Reason:** It only checks if the head is None.

---

## 3. `prepend(self, data)`

**T(n):** 1  
**O(1)**

**Reason:** It adds a node at the beginning without looping through the list.

---

## 4. `append(self, data)`

**T(n):** n  
**O(n)**

**Reason:** In the worst case, it must travel to the end of the list.

---

## 5. `insert_after(self, target, data)`

**T(n):** 1  
**O(1)**

**Reason:** The target node is already given, so it only changes a few links.

---

## 6. `delete(self, target)`

**T(n):** n  
**O(n)**

**Reason:** In the worst case, it must search the whole list to find the target node.

---

## 7. `search(self, data)`

**T(n):** n  
**O(n)**

**Reason:** In the worst case, the data is at the end of the list or is not in the list.

---

## 8. `size(self)`

**T(n):** n  
**O(n)**

**Reason:** It counts every node in the list.

---

## 9. `to_list(self)`

**T(n):** n  
**O(n)**

**Reason:** It visits every node and copies the data into a Python list.

---

## 10. `print(self)`

**T(n):** n  
**O(n)**

**Reason:** It visits every node and prints each value.
```