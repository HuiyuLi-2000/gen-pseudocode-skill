# gen-pseudocode-skill

Reconstruct **publication-quality LaTeX pseudocode** (algorithm2e) from academic papers, source code, and research projects.

For AI/ML engineers and researchers who need to convert messy code or paper descriptions into clean, submit-ready algorithm pseudocode for top venues.

---

## What It Does

Takes raw inputs:
- Paper methodology sections
- Source code repositories
- Research notes

And produces:
- Compilable LaTeX (`algorithm2e`)
- Complexity analysis
- Publication-ready pseudocode matching venue conventions

---

## Quick Start

```
algo-reconstruct/
├── SKILL.md              # Core workflow & rules
├── references/
│   ├── notation.md       # Symbol mapping (code → LaTeX)
│   └── style_guide.md    # Per-venue style expectations
└── scripts/
    └── compile_algo.py   # Compile .tex → PDF
```

### Compile Example

```bash
python scripts/compile_algo.py your_algorithm.tex
```

---

## Workflow

```
1. Gather Sources
   Paper methodology → Appendix → Source code

2. Identify Novelty
   Pinpoint the core contribution (not just a training loop)

3. Select Structure
   Single unified algorithm OR multi-algorithm by stage

4. Draft Pseudocode
   Use notation.md for symbol mapping

5. Compile
   Run compile_algo.py, fix errors until PDF succeeds

6. Deliver
   Rationale → LaTeX → Complexity Analysis → Compilation Result
```

---

## Source Priority

| Priority | Source | Use for |
|----------|--------|---------|
| 1 | Paper methodology | Core logic, algorithmic flow |
| 2 | Appendix / supplementary | Missing steps, detailed procedures |
| 3 | Source code | Clarify ambiguity, verify consistency |

> If code conflicts with paper → trust paper, note discrepancy.

---

## Abstraction Level: METHOD-LEVEL

**Include:**
- Core methodological pipeline
- Key optimization logic
- Important mathematical transformations
- Novel modules
- Training / inference stages

**Exclude:**
- Low-level tensor ops (`tensor.cuda()`, `batch.to(device)`)
- Framework APIs (`optimizer.zero_grad()`, `loss.backward()`)
- Engineering clutter

---

## Notation Mapping

Key conversions from programming to scientific notation:

| Programming | LaTeX | Context |
|-------------|-------|---------|
| `model(x)` | `f_{\theta}(\mathbf{x})` | Forward pass |
| `prediction` | `\hat{y}` | Output |
| `label` | `y` | Ground truth |
| `loss` | `\mathcal{L}` | Objective |
| `learning_rate` | `\eta` | Hyperparameter |
| `embedding(x)` | `\mathbf{e}_x` | Embedding |
| `weights` | `\mathbf{W}` | Parameter matrix |
| `features` | `\mathbf{X}` | Feature matrix |
| `gradient` | `\nabla_{\theta}` | Gradient |
| `params` | `\theta` | Parameter set |

Full mapping: [`references/notation.md`](references/notation.md)

---

## Venue Compatibility

| Venue | Style |
|-------|-------|
| NeurIPS / ICML / ICLR | Compact single-algorithm, concise captions |
| AAAI / KDD / WWW | More procedural detail, separate preprocessing |
| TPAMI / TKDE / TNNLS | Formal notation, detailed line-by-line steps |
| JAMIA / NPJ Digital Medicine | Clinical terminology, domain-specific workflow |

Full guide: [`references/style_guide.md`](references/style_guide.md)

---

## Example

### Bad (Code Translation)
```latex
\ForEach{batch in DataLoader}{
    optimizer.zeroGrad()
    logits $\leftarrow$ model(batch)
    loss $\leftarrow$ criterion(logits, labels)
    loss.backward()
    optimizer.step()
}
```

### Good (Method-Level Abstraction)
```latex
\ForEach{mini-batch $(\mathbf{X}, \mathbf{y}) \sim \mathcal{D}$}{
    $\hat{\mathbf{y}} \leftarrow f_{\theta}(\mathbf{X})$
    $\mathcal{L} \leftarrow \mathcal{L}(\hat{\mathbf{y}}, \mathbf{y}) + \lambda \|\theta\|_2^2$
    $\theta \leftarrow \theta - \eta \nabla_{\theta} \mathcal{L}$
}
```

---

## Quality Checklist

Before finalizing:
- [ ] Looks like top-tier conference pseudocode
- [ ] Reflects methodology, not source code
- [ ] Highlights novelty
- [ ] Scientifically concise
- [ ] Mathematical notation normalized
- [ ] No engineering clutter
- [ ] Fully compilable
- [ ] Publication-ready

---


## Dependencies

- LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
- Python 3.7+ (for compile script)
- `algorithm2e` package

---

## License
MIT
