from evaluators.base import Evaluator

class RougeEvaluator(Evaluator):
    name = "rouge"

    def __call__(self, sample):
        pred = sample["llm_response"].split()
        ref = sample["reference_answer"].split()

        if not pred or not ref:
            return 0.0

        overlap = sum(t in ref for t in pred)
        precision = overlap / len(pred)
        recall = overlap / len(ref)

        return (2 * precision * recall) / (precision + recall) if precision + recall else 0.0
