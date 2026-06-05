#!/usr/bin/env python3
"""Heuristic quality audit for neuromarketing copy drafts."""

import argparse
import json
import re
import sys
from pathlib import Path

CTA_PHRASES = [
    "start",
    "book",
    "buy",
    "try",
    "get",
    "join",
    "apply",
    "download",
    "reserve",
    "shop",
    "subscribe",
    "request",
    "zakazi",
    "rezerviraj",
    "kupi",
    "naruci",
    "preuzmi",
    "prijavi",
    "zatrazi",
    "zapocni",
]

PROOF_MARKERS = [
    "case study",
    "testimonial",
    "review",
    "rated",
    "customers",
    "clients",
    "users",
    "results",
    "data",
    "report",
    "certified",
    "years",
    "studija",
    "recenzija",
    "iskustvo",
    "klijen",
    "kupaca",
    "korisnika",
    "timova",
    "rezultat",
    "pomogao",
    "dokaz",
    "podaci",
    "certifikat",
]

EMOTION_WORDS = [
    "safe",
    "confident",
    "calm",
    "fear",
    "stress",
    "relief",
    "trust",
    "frustrated",
    "worry",
    "proud",
    "mirno",
    "sigurno",
    "samopouzdanje",
    "strah",
    "stres",
    "olaksanje",
    "olaksanje",
    "povjerenje",
    "briga",
    "ponos",
]

RISKY_PHRASES = [
    "guaranteed",
    "risk-free forever",
    "works for everyone",
    "instant",
    "scientifically proven",
    "limited spots",
    "zagarantirano",
    "bez rizika",
    "za svakoga",
    "odmah",
    "dokazano",
    "posljednja prilika",
]

ABSOLUTES = [
    "always",
    "never",
    "everyone",
    "nobody",
    "best",
    "ultimate",
    "all",
    "nikad",
    "uvijek",
    "svi",
    "nitko",
    "najbolji",
    "sve",
]

AUDIENCE_PRONOUNS = [
    "you",
    "your",
    "yours",
    "ti",
    "tebi",
    "tvoj",
    "tvoja",
    "vi",
    "vas",
    "vama",
]

UNIT_MARKERS = [
    "%",
    " eur",
    " usd",
    " hrk",
    " days",
    " day",
    " hours",
    " mins",
    " tjed",
    " dana",
    " sati",
    " min",
]

WORD_RE = re.compile(r"\b[\w'-]+\b", flags=re.UNICODE)


class AuditError(Exception):
    """Raised when audit input is invalid."""


def clamp(value, low=0.0, high=10.0):
    return max(low, min(high, value))


def count_phrase_hits(text_lower, phrases):
    hits = {}
    for phrase in phrases:
        count = text_lower.count(phrase)
        if count:
            hits[phrase] = count
    return hits


def split_sentences(text):
    text = text.strip()
    if not text:
        return []
    raw = re.split(r"(?<=[.!?])\s+", text)
    return [s.strip() for s in raw if s.strip()]


def tokenize(text):
    return WORD_RE.findall(text.lower())


def read_input_text(file_path, inline_text):
    if file_path and inline_text:
        raise AuditError("Use only one input source: --file or --text.")

    if file_path:
        path = Path(file_path)
        if not path.exists():
            raise AuditError(f"File not found: {path}")
        return path.read_text(encoding="utf-8")

    if inline_text:
        return inline_text

    if not sys.stdin.isatty():
        return sys.stdin.read()

    raise AuditError("Provide input with --file, --text, or stdin.")


def score_clarity(avg_sentence_len, long_sentence_ratio, avg_word_len):
    score = 10.0

    if avg_sentence_len > 24:
        score -= 3.5
    elif avg_sentence_len > 20:
        score -= 2.0
    elif avg_sentence_len > 16:
        score -= 0.8

    if long_sentence_ratio > 0.45:
        score -= 3.0
    elif long_sentence_ratio > 0.30:
        score -= 1.8
    elif long_sentence_ratio > 0.20:
        score -= 0.8

    if avg_word_len > 6.5:
        score -= 2.0
    elif avg_word_len > 6.0:
        score -= 1.0

    return clamp(score)


def score_specificity(number_count, unit_count):
    base = 2.0
    score = base + min(5.0, number_count * 1.2) + min(3.0, unit_count * 0.8)
    return clamp(score)


def score_credibility(proof_count):
    score = 2.0 + min(8.0, proof_count * 1.8)
    return clamp(score)


def score_emotion(emotion_count, word_count):
    if word_count == 0:
        return 0.0
    ratio = emotion_count / float(word_count)

    if ratio == 0:
        return 3.0
    if ratio < 0.005:
        return 5.5
    if ratio <= 0.03:
        return 8.5
    if ratio <= 0.06:
        return 7.0
    return 5.0


def score_actionability(cta_count):
    if cta_count == 0:
        return 2.0
    if cta_count == 1:
        return 8.0
    if cta_count <= 3:
        return 9.0
    return 6.5


def score_audience_focus(pronoun_count, word_count):
    if word_count == 0:
        return 0.0
    ratio = pronoun_count / float(word_count)
    if ratio < 0.003:
        return 3.0
    if ratio < 0.01:
        return 6.0
    if ratio <= 0.04:
        return 8.5
    return 7.5


def score_compliance(risky_count, absolute_count):
    penalty = risky_count * 2.3 + absolute_count * 0.6
    return clamp(10.0 - penalty)


def score_fluency(avg_sentence_len, question_count):
    score = 8.0
    if avg_sentence_len <= 18:
        score += 1.0
    if avg_sentence_len > 24:
        score -= 1.5

    if question_count > 4:
        score -= 0.8

    return clamp(score)


def build_recommendations(scores, risky_hits, proof_hits, cta_hits, number_count):
    recommendations = []

    if scores["clarity"] < 7:
        recommendations.append("Shorten long sentences and replace abstract terms with concrete language.")
    if scores["audience_focus"] < 7:
        recommendations.append("Increase audience mirroring with second-person language and explicit context.")
    if scores["specificity"] < 7:
        recommendations.append("Add bounded specifics: numbers, timeframe, mechanism, or constraints.")
    if scores["credibility"] < 7:
        recommendations.append("Add proof elements: data points, testimonials, or concrete case outcomes.")
    if scores["actionability"] < 7:
        recommendations.append("Use one clear CTA with a low-friction next step.")
    if scores["compliance"] < 8:
        recommendations.append("Remove absolute/risky claims and replace them with qualified, evidence-based phrasing.")

    if not proof_hits:
        recommendations.append("No proof markers detected; support major claims with evidence.")
    if not cta_hits:
        recommendations.append("No CTA markers detected; add an explicit action request.")
    if number_count == 0:
        recommendations.append("No numeric specificity detected; add at least one concrete number or timeframe.")
    if risky_hits:
        risky_list = ", ".join(sorted(risky_hits.keys())[:4])
        recommendations.append(f"Risky phrases detected: {risky_list}. Replace with safer alternatives.")

    return recommendations


def weighted_total(scores):
    weights = {
        "clarity": 15,
        "audience_focus": 15,
        "specificity": 10,
        "credibility": 15,
        "emotion": 10,
        "actionability": 10,
        "fluency": 10,
        "compliance": 15,
    }

    total = 0.0
    for key, weight in weights.items():
        total += scores[key] * weight
    return round(total / 10.0, 1)


def audit_copy(text):
    text = text.strip()
    if not text:
        raise AuditError("Input text is empty.")

    text_lower = text.lower()
    sentences = split_sentences(text)
    words = tokenize(text)

    sentence_lengths = [len(tokenize(sentence)) for sentence in sentences if sentence.strip()]
    avg_sentence_len = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0.0
    long_sentence_ratio = 0.0
    if sentence_lengths:
        long_sentence_ratio = len([n for n in sentence_lengths if n >= 22]) / float(len(sentence_lengths))

    avg_word_len = sum(len(word) for word in words) / len(words) if words else 0.0
    question_count = text.count("?")
    number_count = len(re.findall(r"\b\d+[\d.,]*\b", text))
    unit_count = sum(1 for marker in UNIT_MARKERS if marker in text_lower)

    cta_hits = count_phrase_hits(text_lower, CTA_PHRASES)
    proof_hits = count_phrase_hits(text_lower, PROOF_MARKERS)
    emotion_hits = count_phrase_hits(text_lower, EMOTION_WORDS)
    risky_hits = count_phrase_hits(text_lower, RISKY_PHRASES)
    absolute_hits = count_phrase_hits(text_lower, ABSOLUTES)
    audience_hits = count_phrase_hits(text_lower, AUDIENCE_PRONOUNS)

    scores = {
        "clarity": score_clarity(avg_sentence_len, long_sentence_ratio, avg_word_len),
        "audience_focus": score_audience_focus(sum(audience_hits.values()), len(words)),
        "specificity": score_specificity(number_count, unit_count),
        "credibility": score_credibility(sum(proof_hits.values())),
        "emotion": score_emotion(sum(emotion_hits.values()), len(words)),
        "actionability": score_actionability(sum(cta_hits.values())),
        "fluency": score_fluency(avg_sentence_len, question_count),
        "compliance": score_compliance(sum(risky_hits.values()), sum(absolute_hits.values())),
    }

    report = {
        "metrics": {
            "word_count": len(words),
            "sentence_count": len(sentences),
            "avg_sentence_length": round(avg_sentence_len, 2),
            "avg_word_length": round(avg_word_len, 2),
            "long_sentence_ratio": round(long_sentence_ratio, 3),
            "question_count": question_count,
            "number_count": number_count,
            "unit_marker_count": unit_count,
        },
        "signals": {
            "cta_hits": cta_hits,
            "proof_hits": proof_hits,
            "emotion_hits": emotion_hits,
            "risky_hits": risky_hits,
            "absolute_hits": absolute_hits,
            "audience_hits": audience_hits,
        },
        "scores": {k: round(v, 1) for k, v in scores.items()},
    }

    report["total_score"] = weighted_total(scores)
    report["quality_gate_passed"] = report["total_score"] >= 85.0 and report["scores"]["compliance"] >= 8.0
    report["recommendations"] = build_recommendations(
        report["scores"],
        risky_hits,
        proof_hits,
        cta_hits,
        number_count,
    )

    return report


def print_human_report(report):
    metrics = report["metrics"]
    scores = report["scores"]

    print("Neuromarketing Copy Audit")
    print("=========================")
    print(f"Total score: {report['total_score']}/100")
    print(f"Quality gate passed: {'yes' if report['quality_gate_passed'] else 'no'}")
    print()

    print("Core metrics")
    print(f"- Word count: {metrics['word_count']}")
    print(f"- Sentence count: {metrics['sentence_count']}")
    print(f"- Avg sentence length: {metrics['avg_sentence_length']}")
    print(f"- Avg word length: {metrics['avg_word_length']}")
    print(f"- Number count: {metrics['number_count']}")
    print()

    print("Dimension scores (0-10)")
    ordered_keys = [
        "clarity",
        "audience_focus",
        "specificity",
        "credibility",
        "emotion",
        "actionability",
        "fluency",
        "compliance",
    ]
    for key in ordered_keys:
        print(f"- {key}: {scores[key]}")
    print()

    print("Recommendations")
    if report["recommendations"]:
        for item in report["recommendations"]:
            print(f"- {item}")
    else:
        print("- No major issues detected.")


def main():
    parser = argparse.ArgumentParser(
        description="Audit copy text with neuromarketing-oriented heuristics.",
    )
    parser.add_argument("--file", help="Path to text file to audit")
    parser.add_argument("--text", help="Inline text to audit")
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    args = parser.parse_args()

    try:
        text = read_input_text(args.file, args.text)
        report = audit_copy(text)
    except AuditError as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        sys.exit(1)

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print_human_report(report)


if __name__ == "__main__":
    main()
