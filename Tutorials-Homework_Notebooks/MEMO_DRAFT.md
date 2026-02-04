# Research Memo: Agentic Interventions and Language Model Predictability

## Research Question

Which agentic interventions—prompt-based reframing, multi-agent critique, or retrieval-augmented generation—are capable of making otherwise predictable research abstracts deviate most systematically from a vanilla language model baseline, as measured by perplexity under a fixed evaluator model?

## Research Design

This study implements a **within-abstract experimental design** that treats large language model outputs as observations under manipulable conditions (Broska, Howes, & van Loon, 2025). Following their "mixed subjects" framework, I hold the model constant (GPT-4o-mini) and the input text constant (12 MACSS research abstracts), while systematically varying the agentic structure surrounding generation. This approach treats the model as a "potentially informative subject" whose responses reveal how different intervention mechanisms shape output distributions.

The baseline condition uses zero-shot prompting for clarity, establishing a vanilla LLM behavior pattern. Four intervention conditions manipulate the generation process: **few-shot prompting** (providing exemplars), **actor-critic architecture** (introducing structured critique and revision cycles), **chain-of-thought prompting** (encouraging explicit reasoning), and **retrieval-augmented generation** (modifying the information environment). These interventions reflect design mechanisms shown to alter LLM outputs without changing model weights (Costello et al., 2024; Potter et al., 2024; Lai et al., 2024).

The outcome measure is **perplexity under GPT-2**, capturing deviation from expected language patterns. Consistent with Horton's (2023) "Homo Silicus" framework, I interpret perplexity diagnostically rather than causally: higher perplexity indicates less predictable, more distinctive outputs; lower perplexity indicates convergence toward standardized academic language. This measure operationalizes "surprise" as distributional deviation from baseline expectations.

The design extends prior work by systematically comparing agentic mechanisms under controlled conditions. While Costello et al. (2024) demonstrate that dialogue structures can shift beliefs, and Potter et al. (2024) show how prompting reveals bias, this design isolates which structural interventions most reliably move outputs away from vanilla model behavior when applied to identical inputs.

## Visual Element: Pilot Data Analysis

The figure shows within-abstract perplexity trajectories across five conditions for 12 abstracts. Key findings: (1) Original abstracts exhibit highest perplexity (mean ≈ 80), indicating naturalistic academic writing is relatively unpredictable. (2) All clarity-seeking interventions substantially reduce perplexity: zero-shot baseline (≈35), few-shot (≈38), actor-critic (≈32), and chain-of-thought (≈34). (3) Individual abstracts show consistent downward trajectories, with minimal rank-order changes across conditions. (4) Actor-critic produces the lowest mean perplexity, suggesting structured critique most effectively standardizes language.

These results reveal that standard agentic interventions **regularize** rather than diversify outputs. Every intervention pushes abstracts toward more predictable patterns, with multi-turn critique showing the strongest effect. This finding challenges assumptions that agentic complexity increases output diversity—instead, current architectures converge on stereotyped academic prose.

**Next steps**: The homework will pilot **surprise-seeking interventions** that explicitly encourage deviation from conventions: provocative reframing prompts, multi-agent debate with contrarian perspectives, and RAG with "anti-boring" documents. If these increase perplexity while maintaining accuracy, they would demonstrate that agentic design can systematically enable surprising outputs—answering whether LLMs can generate genuinely unexpected research framings when appropriately structured.

---

**Word count**: 493 words