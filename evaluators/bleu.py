from evaluators.base import Evaluator

class BLEUEvaluator(Evaluator):
    name = "bleu"

    def __call__(self, sample):
        pred = sample["llm_response"].split()
        ref = set(sample["reference_answer"].split())

        if not pred:
            return 0.0

        return sum(t in ref for t in pred) / len(pred)
