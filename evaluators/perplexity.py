import torch
import torch.nn.functional as F
from evaluators.base import Evaluator


class PerplexityEvaluator(Evaluator):
    name = "perplexity"

    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer

    def __call__(self, sample):
        text = sample["llm_response"]

        input_ids = self.tokenizer(text).unsqueeze(0)

        if input_ids.size(1) < 2:
            return 0.0

        with torch.no_grad():
            outputs = self.model(input_ids)
            logits = outputs.logits

            shift_logits = logits[:, :-1, :].contiguous()
            shift_labels = input_ids[:, 1:].contiguous()

            loss = F.cross_entropy(
                shift_logits.view(-1, shift_logits.size(-1)),
                shift_labels.view(-1),
            )

        return float(torch.exp(loss))
