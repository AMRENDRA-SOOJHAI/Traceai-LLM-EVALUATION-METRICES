# 📊 LLM Evaluation Metrics

This document explains the **most commonly used evaluation metrics for Large Language Models (LLMs)**.
These metrics help measure **fluency, accuracy, similarity, coverage, and semantic understanding** of generated text.

---

## 🔹 1. Perplexity

### 📌 What is Perplexity?

Perplexity measures **how confused a language model is when predicting text**.

**In simple terms:**
Perplexity tells you **how many choices, on average, the model thinks it has for the next word**.

---

### 🔍 Interpretation

* **Low Perplexity** → Model is confident & predictable
* **High Perplexity** → Model is uncertain & confused

| Perplexity Value | Interpretation              |
| ---------------- | --------------------------- |
| **1 – 10**       | Excellent language modeling |
| **10 – 50**      | Reasonable fluency          |
| **50 – 100+**    | Poor prediction             |

---

### 🧮 Formula

```math
Perplexity = exp\left(-\frac{1}{N} \sum_{i=1}^{N} \log P(w_i)\right)
```

**Where:**

* `N` = Total number of tokens
* `w_i` = i-th token
* `P(w_i)` = Probability assigned to token `w_i`

---

### ✅ Key Insight

Perplexity is the **exponential of the average negative log-probability** assigned to the correct next tokens.

➡️ **Lower perplexity = better language understanding**

---

## 🔹 2. BLEU (Bilingual Evaluation Understudy)

### 📌 What is BLEU?

BLEU measures **how similar a generated text is to a reference (correct) text**, based on **n-gram overlap**.

**In simple terms:**
BLEU checks **how much the model’s output looks like a known good answer**.

---

### 🧠 How BLEU Works

BLEU evaluates **n-gram precision**:

* **Unigram** → Single words
* **Bigram** → 2-word sequences
* **Trigram** → 3-word sequences

---

### 📊 BLEU Score Interpretation

| BLEU Score    | Meaning                 |
| ------------- | ----------------------- |
| **0.7 – 1.0** | Very close to reference |
| **0.4 – 0.7** | Reasonably similar      |
| **0.2 – 0.4** | Weak similarity         |
| **< 0.2**     | Poor match              |

---

### 🧮 BLEU Formula

```math
BLEU = BP \cdot \exp\left(\sum_{n=1}^{N} w_n \log p_n\right)
```

**Where:**

* `p_n` = n-gram precision
* `w_n` = n-gram weight (usually uniform)
* `BP` = Brevity Penalty

---

### ⚠️ Notes

* BLEU is **precision-focused**
* Penalizes overly short outputs using **Brevity Penalty**
* Less effective for paraphrasing or creative text

---

## 🔹 3. ROUGE (Recall-Oriented Understudy for Gisting Evaluation)

### 📌 What is ROUGE?

ROUGE measures **overlap between generated text and reference text**, with a **focus on recall**.

In GenAI tasks, **missing important information is worse than adding extra words** — ROUGE captures this.

---

### 🔍 Types of ROUGE

#### 🔸 ROUGE-N (n-gram overlap)

Measures how many **n-grams from the reference** appear in the generated text.

```math
ROUGE\text{-}N = \frac{\text{Matching n-grams}}{\text{Total n-grams in reference}}
```

---

#### 🔸 ROUGE-L (Longest Common Subsequence)

* Measures the **longest common subsequence (LCS)**
* Captures **sentence structure & fluency**

---

#### 🔸 ROUGE-S (Skip-Bigram)

* Matches word pairs allowing gaps
* Useful for flexible phrasing (less common)

---

### 📊 ROUGE Metrics

| Metric        | Meaning                             |
| ------------- | ----------------------------------- |
| **Precision** | How much generated text is relevant |
| **Recall**    | How much reference text is covered  |
| **F1 Score**  | Balance between precision & recall  |

---

## 🔹 4. BERTScore

### 📌 What is BERTScore?

BERTScore measures **semantic similarity** using **contextual embeddings** from pretrained transformer models
(e.g., **BERT**, **RoBERTa**).

---

### 🚀 Why BERTScore?

Unlike BLEU or ROUGE, BERTScore:

* ✅ Does **not rely on exact word overlap**
* ✅ Understands **meaning and paraphrases**
* ✅ Works better for **modern LLM outputs**

---

### 🧠 How It Works

1. Encode tokens using contextual embeddings
2. Match generated tokens with reference tokens
3. Compute similarity using **cosine similarity**

---

### 📊 BERTScore Outputs

* **Precision** – Semantic relevance of generated text
* **Recall** – Semantic coverage of reference text
* **F1 Score** – Overall semantic similarity

✨ Two sentences with the same meaning but different words can still achieve a **high BERTScore**.

---

## 🧠 Summary Comparison

| Metric         | Focus      | Best For           |
| -------------- | ---------- | ------------------ |
| **Perplexity** | Confidence | Language modeling  |
| **BLEU**       | Precision  | Translation        |
| **ROUGE**      | Recall     | Summarization      |
| **BERTScore**  | Semantics  | Modern GenAI tasks |

---
