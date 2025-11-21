# Big Data Exercise 1: Hadoop Word Count on AWS EMR

This repository contains the Python scripts (`mapper.py`, `reducer.py`) and answers for the Hadoop MapReduce training exercise.

**Students:**
* Guy First ID 322372681
* Noa Levy ID 318304904

## 🛠️ Exercise 1: Analyzing Job Counters

### Initial Job Run (Default Reducers: 3)

| Counter | Value | Source |
| :--- | :--- | :--- |
| Launched map tasks | 9 | Job Counters |
| Launched reduce tasks | 3 | Job Counters |
| Merged Map outputs | 27 | Map-Reduce Framework |

---

### Second Job Run (with `-numReduceTasks 6`)

| Counter | Value | Source |
| :--- | :--- | :--- |
| Launched map tasks | 9 | Job Counters |
| Launched reduce tasks | 6 | Job Counters |
| Merged Map outputs | 54 | Map-Reduce Framework |

---

### Answers for Exercise 1

**Q1. How many files are there now?**
After the change in the reducers number, there are **7 files** (one of which is the `_SUCCESS` status file).

**Q2. Did number of mapper change?**
No, it stayed **9**.

**Q3. Did number of reducers changed?**
Yes, it changed to **6** as we specified it in the CLI using `-numReduceTasks 6`.

**Q4. Did number of output files change? Why?**
Yes, it changed because we changed the reducer number. Each reducer creates one file, so we got 6 reducers + 1 `_SUCCESS` file = 7 files in total.

**Q5. What does the value of 'Merged Map outputs' represents and how is it calculated?**
The value of 'Merged Map outputs' tracks the total number of times intermediate data files from the Map tasks were combined (merged) on the local disk before being sent to the Reducers. The total value is calculated as the product of the launched map tasks and the launched reduce tasks.

---

## 🧼 Exercise 2: Data Cleaning and Standardization

The goal was to:
1.  Strip trailing commas and dots at the end of the words.
2.  Treat upper and lower case words the same (case-insensitive).

### Answer to Pre-Task Question

**Q1. Is your change in the mapper or in the reducer?**
The code is changed in the **Mapper**. The Mapper is the one that collects the very first information, and this is where the logic for data standardization (lowercase and stripping punctuation) has to be changed.

### Results Output (Top of the List)

| Word | Count |
| :--- | :--- |
| his | 14000 |
| that | 15360 |
| he | 17589 |
| in | 20339 |
| a | 20738 |
| to | 31891 |
| of | 34588 |
| and | 42768 |
| the | 74369 |

**Mapper Code:** [https://github.com/GuyFirst/Big-Data-exercise-1-Hadoop/blob/main/mapper.py](https://github.com/GuyFirst/Big-Data-exercise-1-Hadoop/blob/main/mapper.py)

---

## 🏆 Exercise 3: Top 3 Word Counts

The goal was to get only the first 3 highest scores of the word count, using the parameter `-numReduceTasks 1`.

### Answer to Pre-Task Question

**Q1. Is your change in the mapper or in the reducer?**
The code change is primarily in the **Reducer**. The Reducer is where all word counts are aggregated, making it the appropriate place to perform the global sorting and selection of the top 3 results.

### Final Output

The output of the MapReduce job using `-numReduceTasks 1` and modified Reducer logic:

| Word | Count |
| :--- | :--- |
| the | 74369 |
| and | 42768 |
| of | 34588 |

**Reducer Code:** [https://github.com/GuyFirst/Big-Data-exercise-1-Hadoop/blob/main/reducer.py](https://github.com/GuyFirst/Big-Data-exercise-1-Hadoop/blob/main/reducer.py)
