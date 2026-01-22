# def run_evaluators(sample, evaluators, context=None):
#     scores = {}
#     context = context or {}

#     for evaluator in evaluators:
#         score = evaluator(sample, context)
#         scores[evaluator.name] = score

#         # store intermediate results
#         context[evaluator.name] = score

#     return scores

def run_evaluators(sample, evaluators):
    """
    Runs all evaluators independently on a single sample.
    """
    return {
        evaluator.name: evaluator(sample)
        for evaluator in evaluators
    }
