---
name: algo-reconstruct
description: Reconstruct publication-quality LaTeX pseudocode (algorithm2e) from academic papers, source code repositories, and research projects. Use when the user asks to generate pseudocode, write algorithm LaTeX, convert code to algorithm, reconstruct algorithm from paper, or any task involving scientific algorithm representation for SCI journals or AI/ML conferences (NeurIPS, ICML, ICLR, AAAI, KDD, TPAMI, TKDE, etc.). Triggers include "pseudocode", "algorithm", "algo2e", "algorithm2e", "write algorithm", "generate algorithm", "reconstruct algorithm", "论文算法", "伪代码".
---

# Algorithm Reconstructor

Reconstruct methodological logic from papers and code into publication-grade LaTeX pseudocode.

## Workflow

1. **Gather sources** — Read paper methodology section, appendix, and source code. Prioritize paper over code.
2. **Identify novelty** — Pinpoint the core contribution. Do NOT reduce it to a generic training loop.
3. **Select structure** — Single unified algorithm, or multi-algorithm by stage. Adapt to paper's natural decomposition.
4. **Draft pseudocode** — Follow style rules below. Use `references/notation.md` for symbol mapping.
5. **Compile** — Run `scripts/compile_algo.py` on the generated `.tex`. Fix errors until PDF succeeds.
6. **Output** — Deliver: Rationale → LaTeX → Complexity Analysis → Compilation Result.

## Source Priority

| Priority | Source | Use for |
|----------|--------|---------|
| 1 | Paper methodology | Core logic, algorithmic flow |
| 2 | Appendix / supplementary | Missing steps, detailed procedures |
| 3 | Source code | Clarify ambiguity, verify consistency |

If code conflicts with paper → trust paper, note discrepancy in Rationale.

## Abstraction Level

**METHOD-LEVEL** pseudocode. Include:
- Core methodological pipeline
- Key optimization logic
- Important mathematical transformations
- Novel modules
- Training / inference stages

Exclude:
- Low-level tensor ops (`tensor.cuda()`, `batch.to(device)`)
- Framework APIs (`optimizer.zero_grad()`, `loss.backward()`)
- Engineering clutter

If the contribution IS a specific module → elaborate that module sufficiently.

## Pseudocode Style

Package: `\usepackage[ruled,vlined,linesnumbered]{algorithm2e}`

Conventions:
- `\KwIn` / `\KwOut` for input/output
- Line numbering enabled
- Scientific notation over programming notation (see `references/notation.md`)
- Concise mathematical wording

## Output Format

Always output in this order:

### # Rationale
- How algorithm was reconstructed
- Abstraction decisions and assumptions
- Paper-code discrepancies

### # LaTeX Pseudocode
Full compilable LaTeX snippet. Must compile directly.

### # Complexity Analysis
- Algorithm intuition (2-3 sentences)
- Time complexity: O(...)
- Space complexity: O(...)
- State assumptions if derivation is uncertain

### # Compilation Result
- Engine used
- Success/failure
- PDF path
- Fixes applied

## Quality Checklist

Before finalizing, verify:
- [ ] Looks like top-tier conference pseudocode
- [ ] Reflects methodology, not source code
- [ ] Highlights novelty
- [ ] Scientifically concise
- [ ] Mathematical notation normalized
- [ ] No engineering clutter
- [ ] Fully compilable
- [ ] Publication-ready

## Resources

- `references/notation.md` — Symbol mapping and LaTeX conventions
- `references/style_guide.md` — Per-venue style expectations and examples
- `scripts/compile_algo.py` — Compile `.tex` to PDF with auto-retry
