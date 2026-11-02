import re
import string
from collections import Counter
from typing import List, Dict, Set, Tuple


STOPWORDS = {
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't",
    "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by",
    "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't",
    "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have",
    "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself",
    "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into",
    "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my",
    "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our",
    "ours", "ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's",
    "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs",
    "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're",
    "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't",
    "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's",
    "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't",
    "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself",
    "yourselves"
}


def normalize_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[\r\n\t]+', ' ', text)
    text = re.sub(r'[^\w\s\.\+\#\-]', ' ', text)
    return ' '.join(text.split())


def extract_tokens(text: str) -> List[str]:
    cleaned = normalize_text(text)
    raw_tokens = re.findall(r'\b[a-zA-Z0-9\+\#\.\-]{2,}\b', cleaned)
    return [t for t in raw_tokens if t not in STOPWORDS and not t.isdigit()]


def extract_keywords(text: str, top_n: int = 25) -> List[Tuple[str, int]]:
    tokens = extract_tokens(text)
    counts = Counter(tokens)
    return counts.most_common(top_n)


def compute_jaccard_similarity(set_a: Set[str], set_b: Set[str]) -> float:
    if not set_a or not set_b:
        return 0.0
    intersection = len(set_a.intersection(set_b))
    union = len(set_a.union(set_b))
    return float(intersection) / float(union) if union > 0 else 0.0


def calculate_match_score(resume_text: str, jd_text: str) -> Dict[str, object]:
    resume_tokens = extract_tokens(resume_text)
    jd_tokens = extract_tokens(jd_text)

    resume_set = set(resume_tokens)
    jd_set = set(jd_tokens)

    matched_keywords = sorted(list(resume_set.intersection(jd_set)))
    missing_keywords = sorted(list(jd_set.difference(resume_set)))

    jaccard = compute_jaccard_similarity(resume_set, jd_set)

    jd_counts = Counter(jd_tokens)
    total_jd_weight = sum(jd_counts.values()) if jd_counts else 1
    matched_weight = sum(jd_counts[kw] for kw in matched_keywords)
    coverage_ratio = float(matched_weight) / float(total_jd_weight)

    heuristic_score = int(min(100, max(0, round((coverage_ratio * 70.0) + (jaccard * 30.0) * 1.5))))

    return {
        "match_score": heuristic_score,
        "matched_count": len(matched_keywords),
        "missing_count": len(missing_keywords),
        "top_matched": matched_keywords[:15],
        "top_missing": missing_keywords[:15],
        "jaccard_index": round(jaccard, 4)
    }

