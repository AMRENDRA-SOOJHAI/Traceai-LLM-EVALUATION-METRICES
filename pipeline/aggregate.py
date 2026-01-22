def aggregate(results):

    def avg(key):
        values = [i[key] for i in results]
        return round(sum(values) / len(values), 4)
    
    return {
        "avg_bleu": avg("bleu"),
        "avg_rouge": avg("rouge"),
        "avg_perplexity": avg("perplexity"),
        "avg_fluency": avg("fluency")
    }
