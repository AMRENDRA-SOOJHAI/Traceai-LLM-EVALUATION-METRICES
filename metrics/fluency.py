import math

def compute_fluency(perplexity):
    """
    Log-scaled fluency mapping.
    Stable even for very large perplexity.
    """
    if perplexity <= 0:
        return 1.0

    return 1 / (1 + math.log(perplexity))
