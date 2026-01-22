import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from evaluators.bleu import BLEUEvaluator
from evaluators.rouge import RougeEvaluator
from evaluators.perplexity import PerplexityEvaluator

from pipeline.evaluate import run_evaluators
from pipeline.aggregate import aggregate
from metrics.fluency import compute_fluency


def main_llm_evaluation(
    samples: list,
    model_name: str = "sshleifer/tiny-gpt2"
):
    # ==============================
    # model & tokenizer

    tokenizer_hf = AutoTokenizer.from_pretrained(model_name)
    model_hf = AutoModelForCausalLM.from_pretrained(model_name)
    model_hf.eval()

    # ==============================
    # Tokenizer wrapper (simple)

    def tokenize(text: str) -> torch.Tensor:
        return tokenizer_hf(
            text,
            return_tensors="pt"
        )["input_ids"][0]

    # ==============================
    # Evaluators

    evaluators = [
        BLEUEvaluator(),
        RougeEvaluator(),
        PerplexityEvaluator(
            model=model_hf,
            tokenizer=tokenize
        ),
    ]

    # ==============================
    # Run evaluation

    per_sample_results = []

    for sample in samples:
        scores = run_evaluators(sample, evaluators)
        scores["fluency"] = compute_fluency(scores["perplexity"])
        per_sample_results.append(scores)

    # ==============================
    # Daily aggregate

    daily_summary = aggregate(per_sample_results)
    return per_sample_results, daily_summary
