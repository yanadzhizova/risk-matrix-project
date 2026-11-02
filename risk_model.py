"""
Simple customer risk matrix model.

Each customer gets a rating from 1 (Low) to 3 (High) on five risk factors.
The overall risk score is a weighted average of these ratings, and the score
is turned into a risk level: Low, Medium or High.
"""

import numpy as np
import pandas as pd

FACTORS = ["geography", "customer_type", "industry", "product", "channel"]

# Thresholds that split the score range 1-3 into three equal parts
LOW_THRESHOLD = 5 / 3    # about 1.67
HIGH_THRESHOLD = 7 / 3   # about 2.33


def generate_customers(n, probabilities, seed=42):
    """Create n random customers.

    probabilities is a dictionary: factor -> [P(Low), P(Medium), P(High)].
    Every factor is drawn independently. The seed makes the result repeatable.
    """
    rng = np.random.default_rng(seed)
    data = {}
    for factor in FACTORS:
        data[factor] = rng.choice([1, 2, 3], size=n, p=probabilities[factor])
    return pd.DataFrame(data)


def risk_score(customers, weights):
    """Weighted average of the factor ratings: sum of weight * rating."""
    total_weight = sum(weights.values())
    if abs(total_weight - 1) > 1e-9:
        raise ValueError(f"Weights must add up to 1, but they add up to {total_weight}")
    score = 0
    for factor in FACTORS:
        score = score + weights[factor] * customers[factor]
    return score


def risk_level(score):
    """Turn a score into 'Low', 'Medium' or 'High'."""
    # A tiny tolerance so that a score exactly on a threshold goes to the higher level
    score = score + 1e-9
    return pd.cut(
        score,
        bins=[-np.inf, LOW_THRESHOLD, HIGH_THRESHOLD, np.inf],
        labels=["Low", "Medium", "High"],
        right=False,
    )


def has_red_flag(customers):
    """True for customers who are rated High (3) on at least one factor."""
    return (customers[FACTORS] == 3).any(axis=1)


def apply_red_flag_rule(levels, customers):
    """Extra rule: a customer with at least one High factor is never 'Low'.

    Such customers are moved up from Low to Medium. Medium and High stay as they are.
    """
    new_levels = levels.astype(str).copy()
    move_up = has_red_flag(customers) & (new_levels == "Low")
    new_levels[move_up] = "Medium"
    return pd.Categorical(new_levels, categories=["Low", "Medium", "High"])
