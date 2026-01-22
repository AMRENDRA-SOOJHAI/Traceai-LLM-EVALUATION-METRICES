# 📊 LLM Evaluation Metrics

This document explains the **most commonly used evaluation metrics for Large Language Models (LLMs)**.
These metrics help measure **fluency, accuracy, similarity, coverage, and semantic understanding** of generated text.

---

<img width="1027" height="793" alt="image" src="https://github.com/user-attachments/assets/eea55cb0-b620-4f1f-8c42-4b532d6fc20f" />

## 🔹 1. Perplexity

### 📌 What is Perplexity?

Perplexity measures **how confused a language model is when predicting the next token**.

**In simple terms:**
It tells you **how many choices, on average, the model thinks it has for the next word**.

---

### 🔍 Interpretation

| Perplexity Range | Meaning                          |
| ---------------- | -------------------------------- |
| **1 – 10**       | Excellent language modeling      |
| **10 – 50**      | Reasonable fluency               |
| **50 – 100+**    | Poor prediction / high confusion |

* **Low perplexity** → Model is confident
* **High perplexity** → Model is uncertain

---

### 🧮 Formula

```text
Perplexity = exp( - (1 / N) * Σ log P(w_i) )
```

**Where:**

* `N` = total number of tokens
* `w_i` = i-th token
* `P(w_i)` = probability assigned to the correct token

---

### ✅ Key Insight

Perplexity is the **exponential of the average negative log-probability**.

➡️ **Lower perplexity = better language modeling ability**

---

## 🔹 2. Fluency (Derived from Perplexity)

### 📌 What is Fluency?

Fluency measures **how natural, readable, and grammatically correct** a model’s output feels to humans.

In this project, fluency is **derived from perplexity** and normalized into a **0–1 score**.

* **Fluency ≈ 1.0** → Smooth, natural text
* **Fluency ≈ 0.0** → Awkward or broken text

---

### 🔁 Perplexity → Fluency Mapping

| Perplexity Level | Expected Fluency    |
| ---------------- | ------------------- |
| ≤ 10             | ≈ 1.0 (Very fluent) |
| 10 – 50          | Mid-range fluency   |
| ≥ 100            | ≈ 0.0 (Disfluent)   |

---

### 🧮 Fluency Formula (Project Definition)

```text
Fluency = 1 / (1 + exp(0.1 * (Perplexity - 30)))
```

* Centered around **Perplexity = 30** (acceptable quality)
* Output is bounded between **0 and 1**
* **Higher score = more fluent text**

> ⚠️ This is a **project-specific design choice** to make perplexity easier to compare across models.

---

### 📊 Example Interpretation

| Perplexity | Approx. Fluency | Interpretation            |
| ---------- | --------------- | ------------------------- |
| 5          | ≈ 0.97          | Extremely fluent          |
| 20         | ≈ 0.73          | Good fluency              |
| 40         | ≈ 0.27          | Noticeable wording issues |
| 80         | ≈ 0.05          | Highly disfluent          |

---

## 🔹 3. BLEU (Bilingual Evaluation Understudy)

### 📌 What is BLEU?

BLEU measures **how similar a generated text is to a reference text**, using **n-gram overlap**.

**In simple terms:**
BLEU checks **how close the output is to a known correct answer**.

---

### 🧠 How BLEU Works

* Unigram → single words
* Bigram → 2-word sequences
* Trigram → 3-word sequences

BLEU focuses on **precision**, not recall.

---

### 📊 BLEU Score Interpretation

| BLEU Score | Meaning                 |
| ---------: | ----------------------- |
|  0.7 – 1.0 | Very close to reference |
|  0.4 – 0.7 | Reasonably similar      |
|  0.2 – 0.4 | Weak similarity         |
|      < 0.2 | Poor match              |

---

### 🧮 BLEU Formula

```text
BLEU = BP * exp( Σ (w_n * log(p_n)) )
```

**Where:**

* `p_n` = n-gram precision
* `w_n` = n-gram weight
* `BP` = brevity penalty

---

### ⚠️ Limitations

* Precision-focused
* Penalizes paraphrasing
* Weak for creative or open-ended tasks

---

## 🔹 4. ROUGE (Recall-Oriented Understudy for Gisting Evaluation)

### 📌 What is ROUGE?

ROUGE measures **overlap between generated and reference text**, with a **focus on recall**.

It answers:
➡️ *Did the model cover the important information?*

---

### 🔍 ROUGE Variants

#### 🔸 ROUGE-N (n-gram recall)

```text
ROUGE-N = Matching n-grams / Total reference n-grams
```

#### 🔸 ROUGE-L

* Based on **Longest Common Subsequence (LCS)**
* Captures sentence structure

#### 🔸 ROUGE-S

* Skip-bigram matching
* Allows gaps between words

---

### 📊 ROUGE Metrics

| Metric    | Meaning                       |
| --------- | ----------------------------- |
| Precision | Generated content relevance   |
| Recall    | Reference coverage            |
| F1 Score  | Balance of precision & recall |

---

## 🔹 5. BERTScore

### 📌 What is BERTScore?

BERTScore measures **semantic similarity** using **contextual embeddings** from transformer models (BERT, RoBERTa).

---

### 🚀 Why BERTScore?

* ✅ Understands meaning, not just words
* ✅ Handles paraphrases well
* ✅ Better for modern LLM outputs

---

### 🧠 How It Works

1. Encode tokens into embeddings
2. Match tokens using cosine similarity
3. Compute Precision, Recall, and F1

---

### 📊 BERTScore Outputs

| Metric    | Meaning                     |
| --------- | --------------------------- |
| Precision | Semantic relevance          |
| Recall    | Semantic coverage           |
| F1        | Overall semantic similarity |

---

## 🧠 Metric Summary

| Metric     | Measures            | Best Used For      |
| ---------- | ------------------- | ------------------ |
| Perplexity | Model confidence    | Language modeling  |
| Fluency    | Readability         | Human-like quality |
| BLEU       | Precision overlap   | Translation        |
| ROUGE      | Recall overlap      | Summarization      |
| BERTScore  | Semantic similarity | GenAI evaluation   |

---

If you want next:

* 🧪 **Add a “Dummy Model vs Real Model” explanation**
* 📈 **Add sample outputs from your pipeline**
* 🏗 **Convert this into a research-paper style README**

Just say 👍
