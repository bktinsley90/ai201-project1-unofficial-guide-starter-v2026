def judge(question, expects, answer, results) -> bool:
    """
    llm as judge - rapidfuzz
    Judge whether the answer meets the expected criteria.

    Parameters:
    - question: The question being evaluated.
    - expects: The expected answer or criteria.
    - answer: The actual answer produced.
    - results: Additional results or context for evaluation.

    Returns:
    - True if the answer meets the expected criteria, False otherwise.
    """
    # Placeholder implementation, replace with actual logic
    return answer.lower().strip() == expects.lower().strip()
