# ============================================================
# SURPRISE INTERVENTIONS - PASTE INTO COLAB CELL
# Run this AFTER your existing interventions
# Assumes: sampled dataframe, client, GEN_MODEL, TEXT_COL, ID_COL, perplexity() function exist
# ============================================================

import time

# %% INTERVENTION 1: REFRAME (Unexpected Angle)
PROMPT_REFRAME = """Rewrite this research abstract by reframing the research question
from an unexpected angle that challenges conventional assumptions.

Guidelines:
- Keep the same methods and data
- Preserve the core findings
- Reframe WHY this research matters in a surprising way
- Use creative language that departs from standard academic phrasing

ABSTRACT:
{abstract}
"""

print("Running REFRAME intervention...")
sampled["reframe_rewrite"] = ""

for i, row in sampled.iterrows():
    print(f"[{i+1}/{len(sampled)}] Reframe rewriting {row[ID_COL]}...")
    resp = client.chat.completions.create(
        model=GEN_MODEL,
        temperature=0.7,  # Higher temp = more variation
        messages=[
            {"role": "system", "content": "You are a creative academic editor who challenges conventions."},
            {"role": "user", "content": PROMPT_REFRAME.format(abstract=row[TEXT_COL])}
        ]
    )
    sampled.at[i, "reframe_rewrite"] = resp.choices[0].message.content.strip()
    time.sleep(0.5)

sampled["ppl_reframe"] = sampled["reframe_rewrite"].apply(perplexity)
print(f"✓ Mean reframe perplexity: {sampled['ppl_reframe'].mean():.2f}\n")


# %% INTERVENTION 2: PROVOCATIVE (Counterintuitive)
PROMPT_PROVOCATIVE = """Rewrite this abstract to emphasize its most surprising,
counterintuitive, or controversial implications.

Guidelines:
- Lead with the most unexpected finding
- Frame the research as challenging conventional wisdom
- Use bolder, less hedged language (while remaining accurate)
- Emphasize what's DIFFERENT from prior work

ABSTRACT:
{abstract}
"""

print("Running PROVOCATIVE intervention...")
sampled["provocative_rewrite"] = ""

for i, row in sampled.iterrows():
    print(f"[{i+1}/{len(sampled)}] Provocative rewriting {row[ID_COL]}...")
    resp = client.chat.completions.create(
        model=GEN_MODEL,
        temperature=0.7,
        messages=[
            {"role": "system", "content": "You are a bold academic editor who emphasizes surprise."},
            {"role": "user", "content": PROMPT_PROVOCATIVE.format(abstract=row[TEXT_COL])}
        ]
    )
    sampled.at[i, "provocative_rewrite"] = resp.choices[0].message.content.strip()
    time.sleep(0.5)

sampled["ppl_provocative"] = sampled["provocative_rewrite"].apply(perplexity)
print(f"✓ Mean provocative perplexity: {sampled['ppl_provocative'].mean():.2f}\n")


# %% INTERVENTION 3: MULTI-AGENT DEBATE
def rewrite_with_debate(abstract_text):
    """Three agents with different perspectives, then synthesize."""

    # Agent 1: Critical sociologist
    resp1 = client.chat.completions.create(
        model=GEN_MODEL,
        temperature=0.7,
        messages=[
            {"role": "system", "content": "You are a critical sociologist who sees hidden power dynamics."},
            {"role": "user", "content": f"Reframe this from a critical perspective. What hidden assumptions does this reveal?\n\n{abstract_text}"}
        ]
    )
    reframe1 = resp1.choices[0].message.content.strip()

    # Agent 2: Contrarian
    resp2 = client.chat.completions.create(
        model=GEN_MODEL,
        temperature=0.7,
        messages=[
            {"role": "system", "content": "You are a contrarian who questions conventional interpretations."},
            {"role": "user", "content": f"Challenge the conventional interpretation. What alternative could these findings support?\n\n{abstract_text}"}
        ]
    )
    reframe2 = resp2.choices[0].message.content.strip()

    # Agent 3: Synthesizer
    resp3 = client.chat.completions.create(
        model=GEN_MODEL,
        temperature=0.5,
        messages=[
            {"role": "system", "content": "You synthesize perspectives into compelling narratives."},
            {"role": "user", "content": f"""Synthesize these into ONE abstract (150-200 words) that:
- Preserves original methods/data
- Incorporates the most surprising insights
- Uses unexpected framing

ORIGINAL: {abstract_text}

CRITICAL VIEW: {reframe1}

CONTRARIAN VIEW: {reframe2}

Final abstract:"""}
        ]
    )

    return resp3.choices[0].message.content.strip()

print("Running MULTI-AGENT DEBATE intervention...")
sampled["debate_rewrite"] = ""

for i, row in sampled.iterrows():
    print(f"[{i+1}/{len(sampled)}] Multi-agent debate on {row[ID_COL]}...")
    sampled.at[i, "debate_rewrite"] = rewrite_with_debate(row[TEXT_COL])
    time.sleep(1.0)

sampled["ppl_debate"] = sampled["debate_rewrite"].apply(perplexity)
print(f"✓ Mean debate perplexity: {sampled['ppl_debate'].mean():.2f}\n")


# %% COMPARISON VISUALIZATION
import matplotlib.pyplot as plt
import numpy as np

conditions = [
    ("Original", "ppl_original", "gray"),
    ("0-shot\n(baseline)", "ppl_0shot", "steelblue"),
    ("Few-shot", "ppl_fewshot", "steelblue"),
    ("Actor-Critic", "ppl_actor_critic", "steelblue"),
    ("CoT", "ppl_cot", "steelblue"),
    ("Reframe", "ppl_reframe", "coral"),
    ("Provocative", "ppl_provocative", "coral"),
    ("Multi-Agent\nDebate", "ppl_debate", "coral")
]

labels = []
means = []
colors = []

for label, col, color in conditions:
    if col in sampled.columns:
        labels.append(label)
        means.append(sampled[col].mean())
        colors.append(color)

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(range(len(labels)), means, color=colors, alpha=0.7, edgecolor='black')

# Highlight baseline
baseline_idx = labels.index("0-shot\n(baseline)")
ax.axhline(y=means[baseline_idx], color='black', linestyle='--', linewidth=2,
           label='Vanilla baseline', zorder=0)
bars[baseline_idx].set_linewidth(3)

ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, fontsize=11)
ax.set_ylabel('Perplexity (GPT-2)\nHigher = More Surprising', fontsize=13, fontweight='bold')
ax.set_title('Clarity Interventions vs. Surprise Interventions',
             fontsize=15, fontweight='bold')
ax.grid(axis='y', alpha=0.3)

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='steelblue', alpha=0.7, label='Clarity-seeking'),
    Patch(facecolor='coral', alpha=0.7, label='Surprise-seeking'),
    Patch(facecolor='gray', alpha=0.7, label='Original')
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=11)

plt.tight_layout()
plt.savefig('clarity_vs_surprise_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n" + "="*70)
print("SUMMARY TABLE")
print("="*70)

summary_data = []
for label, col, _ in conditions:
    if col in sampled.columns:
        mean_ppl = sampled[col].mean()
        delta = mean_ppl - sampled["ppl_0shot"].mean()
        summary_data.append({
            'Condition': label.replace('\n', ' '),
            'Mean_PPL': round(mean_ppl, 2),
            'Δ_from_baseline': round(delta, 2)
        })

import pandas as pd
summary_df = pd.DataFrame(summary_data)
print(summary_df.to_string(index=False))
print("\nPositive Δ = MORE surprising than vanilla baseline")
print("Negative Δ = LESS surprising than vanilla baseline")
print("="*70)
