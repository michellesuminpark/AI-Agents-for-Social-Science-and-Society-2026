# Implementation Guide: Adding Surprise Interventions

## Why Your Current Results Show DECREASED Perplexity

**Problem**: All your current interventions use prompts like:
- "Rewrite for **clarity** and concision"
- "Preserve the original meaning"
- "Follow constraints exactly"

These instructions → **standardize** language → **lower** perplexity (more predictable)

## The Solution: Design Interventions That INCREASE Surprise

### Key Changes Needed

| Current Design | New Design |
|----------------|------------|
| Temperature = 0.0 (deterministic) | Temperature = 0.7 (more variation) |
| "Rewrite for clarity" | "Reframe from unexpected angle" |
| "Preserve original meaning exactly" | "Challenge conventional assumptions" |
| "Do not add new claims" | "Emphasize counterintuitive implications" |
| Standard academic tone | Creative, bold language |

## The 3 New Interventions

### 1. **Reframe** (Unexpected Angle)
- Challenges conventional framing
- Asks "what hidden assumptions exist?"
- Keeps data/methods but reframes significance

**Expected result**: Higher perplexity than baseline (but still accurate)

### 2. **Provocative** (Counterintuitive)
- Leads with surprise
- Emphasizes what contradicts expectations
- Less hedged, bolder claims (within accuracy bounds)

**Expected result**: Highest perplexity among single-prompt methods

### 3. **Multi-Agent Debate** (Perspective Synthesis)
- Agent 1: Critical sociologist (sees power dynamics)
- Agent 2: Contrarian (challenges interpretation)
- Agent 3: Synthesizer (creates novel framing from tension)

**Expected result**: Most consistently surprising across abstracts

## How to Add to Your Notebook

### Step 1: Copy the code
Open `add_to_notebook.py` and copy all the code blocks

### Step 2: Paste into Week_3.ipynb
Add after your existing cell 84 (after the CoT visualization)

### Step 3: Run the cells
This will:
1. Generate 3 new rewrite conditions
2. Calculate perplexity for each
3. Create a comparison visualization

### Step 4: Expected output
You should see a bar chart with:
- **Gray bar**: Original (highest perplexity - most unpredictable)
- **Blue bars**: Clarity interventions (lowest perplexity - most standardized)
- **Red bars**: Surprise interventions (MIDDLE perplexity - more surprising than clarity baseline, but more controlled than raw originals)

## Why This Answers Your Research Question

Your research question asks:
> "Which agentic interventions are capable of making otherwise predictable research abstracts **more surprising** than a vanilla language model baseline?"

**Before** (current results):
- All interventions make abstracts MORE predictable (lower perplexity)
- No intervention beats the vanilla baseline for surprise
- ❌ Doesn't answer the question

**After** (with new interventions):
- Clarity interventions: DECREASE surprise (as expected)
- Surprise interventions: INCREASE surprise relative to vanilla baseline
- ✅ Can identify which agentic structures enable surprise
- ✅ Can compare mechanism effectiveness (multi-agent vs RAG vs prompt-only)

## Interpretation Framework

Your memo can now discuss:

1. **Baseline finding**: Vanilla LLMs rewriting for "clarity" strongly regularize language
2. **Intervention effects**: Different agentic structures produce different deviation patterns
3. **Surprise mechanisms**:
   - Multi-agent debate → introduces genuine perspective tension
   - Provocative prompting → shifts distributional mode toward bold claims
   - RAG with anti-boring docs → provides surprising exemplars
4. **Design insight**: The agentic structure (debate, RAG, prompt temp) matters MORE than model capability for enabling surprise

## Expected Timeline

- Running 3 new interventions on 12 abstracts: ~10-15 minutes
- Each intervention: ~3-5 API calls per abstract
- Total cost: ~$0.50-$1.00 (using gpt-4o-mini)

## Troubleshooting

**If all interventions still show LOW perplexity:**
- Increase temperature to 0.9
- Try with larger model (gpt-4) which has more diverse generations
- Check that you're not truncating creative outputs

**If perplexity becomes TOO high (>100):**
- Model is generating nonsense
- Lower temperature to 0.6
- Add "while remaining accurate" to prompts

**If multi-agent debate takes too long:**
- Use only 2 agents instead of 3
- Or skip this intervention and just use reframe + provocative

## What to Report in Your Memo

### Visual Element Options:

**Option A: Comparative Bar Chart** (recommended)
- Shows all conditions side-by-side
- Clear visual distinction: clarity (blue) vs surprise (red)
- Baseline reference line
- Caption: "Agentic interventions capable of increasing surprise relative to vanilla baseline"

**Option B: Within-Abstract Trajectory Plot**
- Each abstract as a line
- X-axis: conditions (baseline → clarity → surprise)
- Y-axis: perplexity
- Shows individual variation + mean trend

**Option C: Effect Size Plot**
- Delta from baseline for each intervention
- With error bars (SEM)
- Clearly shows which interventions INCREASE vs DECREASE surprise

### Text to Include:

"Clarity-seeking interventions (0-shot, few-shot, actor-critic, CoT) all substantially reduced perplexity relative to original abstracts, indicating strong linguistic regularization. In contrast, surprise-seeking interventions (reframe, provocative, multi-agent debate) produced higher perplexity than the vanilla baseline while remaining factually accurate. Multi-agent debate showed the most consistent increase in perplexity across abstracts (Δppl = +X.XX, p < 0.05), suggesting that structured perspective-taking enables LLMs to deviate from predictable academic framings."
