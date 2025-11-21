# Big Data Exercise 1: Hadoop Word Count on AWS EMR

This repository contains the Python scripts (`mapper.py`, `reducer.py`) and answers for the Hadoop MapReduce training exercise.

**Students:**
* [cite_start]Guy First ID 322372681 [cite: 191]
* [cite_start]Noa Levy ID 318304904 [cite: 192]

## 🛠️ Exercise 1: Analyzing Job Counters

### Initial Job Run (Default Reducers: 3)

| Counter | Value | Source |
| :--- | :--- | :--- |
| Launched map tasks | [cite_start]9 [cite: 272] | [cite_start]Job Counters [cite: 244] |
| Launched reduce tasks | [cite_start]3 [cite: 273] | [cite_start]Job Counters [cite: 246, 273] |
| Merged Map outputs | [cite_start]27 [cite: 268, 274] | [cite_start]Map-Reduce Framework [cite: 257] |

---

### Second Job Run (with `-numReduceTasks 6`)

| Counter | Value | Source |
| :--- | :--- | :--- |
| Launched map tasks | [cite_start]9 [cite: 286, 315] | [cite_start]Job Counters [cite: 284] |
| Launched reduce tasks | [cite_start]6 [cite: 287, 316] | [cite_start]Job Counters [cite: 284] |
| Merged Map outputs | [cite_start]54 [cite: 313, 317] | [cite_start]Map-Reduce Framework [cite: 298] |

---

### Answers for Exercise 1

**Q1. [cite_start]How many files are there now?** [cite: 318]
[cite_start]After the change in the reducers number, there are **7 files** (one of which is the `_SUCCESS` status file). [cite: 319]

**Q2. [cite_start]Did number of mapper change?** [cite: 320]
[cite_start]No, it stayed **9**. [cite: 321]

**Q3. [cite_start]Did number of reducers changed?** [cite: 322]
[cite_start]Yes, it changed to **6** as we specified it in the CLI using `-numReduceTasks 6`. [cite: 323]

**Q4. Did number of output files change? [cite_start]Why?** [cite: 324]
[cite_start]Yes, it changed because we changed the reducer number[cite: 325]. [cite_start]Each reducer creates one file, so we got 6 reducers + 1 `_SUCCESS` file = 7 files in total[cite: 326].

**Q5. [cite_start]What does the value of 'Merged Map outputs' represents and how is it calculated?** [cite: 327]
[cite_start]The value of 'Merged Map outputs' tracks the total number of times intermediate data files from the Map tasks were combined (merged) on the local disk before being sent to the Reducers[cite: 328]. [cite_start]The total value is calculated as the product of the launched map tasks and the launched reduce tasks[cite: 329].

---

## 🧼 Exercise 2: Data Cleaning and Standardization

The goal was to:
1.  Strip trailing commas and dots at the end of the words.
2.  Treat upper and lower case words the same (case-insensitive).

### Answer to Pre-Task Question

**Q1. [cite_start]Is your change in the mapper or in the reducer?** [cite: 350]
[cite_start]The code is changed in the **Mapper**[cite: 351]. [cite_start]The Mapper is the one that collects the very first information, and this is where the logic for data standardization (lowercase and stripping punctuation) has to be changed[cite: 351, 352].

### Results Output (Top of the List)

| Word | Count |
| :--- | :--- |
| his | [cite_start]14000 [cite: 331, 332] |
| that | [cite_start]15360 [cite: 333, 334] |
| he | [cite_start]17589 [cite: 335, 336] |
| in | [cite_start]20339 [cite: 337, 338] |
| a | [cite_start]20738 [cite: 339, 340] |
| to | [cite_start]31891 [cite: 341, 342] |
| of | [cite_start]34588 [cite: 343, 344] |
| and | [cite_start]42768 [cite: 345, 346] |
| the | [cite_start]74369 [cite: 347, 348] |

[cite_start]**Mapper Code:** [https://github.com/GuyFirst/Big-Data-exercise-1-Hadoop/blob/main/mapper.py](https://github.com/GuyFirst/Big-Data-exercise-1-Hadoop/blob/main/mapper.py) [cite: 354]

---

## 🏆 Exercise 3: Top 3 Word Counts

The goal was to get only the first 3 highest scores of the word count, using the parameter `-numReduceTasks 1`.

### Answer to Pre-Task Question

**Q1. [cite_start]Is your change in the mapper or in the reducer?** [cite: 373]
[cite_start]The code change is primarily in the **Reducer**[cite: 374]. [cite_start]The Reducer is where all word counts are aggregated, making it the appropriate place to perform the global sorting and selection of the top 3 results[cite: 374].

### Final Output

The output of the MapReduce job using `-numReduceTasks 1` and modified Reducer logic:

| Word | Count |
| :--- | :--- |
| the | [cite_start]74369 [cite: 366, 367] |
| and | [cite_start]42768 [cite: 368, 369] |
| of | [cite_start]34588 [cite: 370, 371] |

[cite_start]**Reducer Code:** [https://github.com/GuyFirst/Big-Data-exercise-1-Hadoop/blob/main/reducer.py](https://github.com/GuyFirst/Big-Data-exercise-1-Hadoop/blob/main/reducer.py) [cite: 376]
