import re

from rapidfuzz import fuzz


MATCH_THRESHOLD = 85


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
    expected = str(expects).strip()
    response = str(answer).strip()
    if not expected or not response:
        return False

    expected = re.sub(r"\s+", "", expected.casefold())
    response = re.sub(r"\s+", "", response.casefold())
    score = fuzz.partial_ratio(expected, response)
    return score >= MATCH_THRESHOLD
