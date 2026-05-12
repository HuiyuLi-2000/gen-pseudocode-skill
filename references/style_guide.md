# Style Guide by Venue

## algorithm2e Setup

```latex
\usepackage[ruled,vlined,linesnumbered]{algorithm2e}
```

Minimal compilable template:

```latex
\documentclass{article}
\usepackage[ruled,vlined,linesnumbered]{algorithm2e}
\usepackage{amsmath,amssymb}
\begin{document}
\begin{algorithm}[H]
\caption{Algorithm Title}
\KwIn{Input description}
\KwOut{Output description}
\ForEach{$x \in \mathcal{X}$}{
    $y \leftarrow f(x)$\;
}
\Return{$y$}
\end{algorithm}
\end{document}
```

## Key algorithm2e Commands

| Command | Purpose |
|---------|---------|
| `\KwIn{...}` | Input |
| `\KwOut{...}` | Output |
| `\ForEach{condition}{body}` | For-each loop |
| `\For{condition}{body}` | For loop |
| `\While{condition}{body}` | While loop |
| `\If{condition}{body}` | If |
| `\eIf{condition}{then}{else}` | If-else |
| `\Repeat{condition}{body}` | Repeat-until |
| `\Return{...}` | Return |
| `\tcp{...}` | Inline comment |
| `\tcc{...}` | Block comment |
| `\lForEach{cond}{stmt}` | Line-level for-each |
| `\lFor{cond}{stmt}` | Line-level for |
| `\lIf{cond}{stmt}` | Line-level if |

## Venue-Specific Notes

### NeurIPS / ICML / ICLR
- Prefer compact single-algorithm presentation for core method
- Multi-algorithm acceptable for multi-stage methods
- Caption: concise, descriptive
- Input/Output: always present

### AAAI / KDD / WWW
- May include more procedural detail
- Data preprocessing can be a separate algorithm
- Complexity discussion in text, not in pseudocode

### TPAMI / TKDE / TNNLS
- More formal mathematical notation expected
- Detailed algorithm steps with line-by-line justification
- Often include convergence properties in surrounding text
- Multiple algorithms common (training + inference)

### JAMIA / NPJ Digital Medicine
- Clinical/medical context requires domain-specific terminology
- Algorithm names should reflect clinical workflow
- Include data preprocessing as separate step when relevant

## Anti-Patterns

### Bad: Code Translation
```latex
\ForEach{batch in DataLoader}{
    optimizer.zeroGrad()\;
    logits $\leftarrow$ model(batch)\;
    loss $\leftarrow$ criterion(logits, labels)\;
    loss.backward()\;
    optimizer.step()\;
}
```

### Good: Method-Level Abstraction
```latex
\ForEach{mini-batch $(\mathbf{X}, \mathbf{y}) \sim \mathcal{D}$}{
    $\hat{\mathbf{y}} \leftarrow f_{\theta}(\mathbf{X})$\;
    $\mathcal{L} \leftarrow \mathcal{L}(\hat{\mathbf{y}}, \mathbf{y}) + \lambda \|\theta\|_2^2$\;
    $\theta \leftarrow \theta - \eta \nabla_{\theta} \mathcal{L}$\;
}
```

## Multi-Algorithm Structure

When a paper naturally decomposes into stages:

```
Algorithm 1: Data Preprocessing and Graph Construction
Algorithm 2: Model Training with [Method Name]
Algorithm 3: Inference and Prediction
```

When user requests "full algorithm" → one unified pipeline.

When user requests specific component → generate only that component.

## Line Ending Rules

- Every statement ends with `\;`
- Control flow headers (`\For`, `\While`, `\If`) do NOT end with `\;`
- `\Return` ends with `\;`
- Line-level commands (`\lFor`, `\lIf`, `\lForEach`) do NOT need `\;`
