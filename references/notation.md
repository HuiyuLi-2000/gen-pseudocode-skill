# Notation Mapping

Automatic conversions from programming to scientific notation.

## Symbol Conversions

| Programming | LaTeX | Context |
|-------------|-------|---------|
| `sigmoid(x)` | `\sigma(x)` | Activation |
| `softmax(x)` | `\mathrm{softmax}(x)` | Activation |
| `relu(x)` | `\mathrm{ReLU}(x)` | Activation |
| `prediction` | `\hat{y}` | Output |
| `label` | `y` | Ground truth |
| `loss` | `\mathcal{L}` | Objective |
| `loss_fn(pred, label)` | `\mathcal{L}(\hat{y}, y)` | Loss evaluation |
| `optimizer.step()` | Update $\theta$ via gradient descent | Optimization |
| `learning_rate` | `\eta` | Hyperparameter |
| `epoch` | `t` (or `T` for total) | Iteration |
| `batch_size` | `B` | Batch |
| `hidden_dim` | `d` | Dimensionality |
| `num_layers` | `L` | Architecture |
| `embedding(x)` | `\mathbf{e}_x` or `f_{\mathrm{emb}}(x)` | Embedding |
| `weights` | `\mathbf{W}` | Parameter matrix |
| `bias` | `\mathbf{b}` | Parameter vector |
| `features` | `\mathbf{X}` | Feature matrix |
| `adjacency` | `\mathbf{A}` | Graph structure |
| `mask` | `\mathbf{M}` | Mask matrix |
| `logits` | `\mathbf{z}` | Pre-activation |
| `gradient` | `\nabla_{\theta}` | Gradient |
| `params` | `\theta` | Parameter set |
| `model(x)` | `f_{\theta}(\mathbf{x})` | Forward pass |
| `train_set` | `\mathcal{D}_{\mathrm{train}}` | Dataset |
| `test_set` | `\mathcal{D}_{\mathrm{test}}` | Dataset |
| `val_set` | `\mathcal{D}_{\mathrm{val}}` | Dataset |
| `data_loader` | `\mathcal{D}` | Dataset reference |
| `sample` | `\mathbf{x}_i` | Data point |
| `index` | `i` | Index |
| `num_classes` | `C` | Classification |
| `temperature` | `\tau` | Temperature |
| `alpha`, `beta` | `\alpha`, `\beta` | Coefficients |
| `lambda` | `\lambda` | Regularization |
| `epsilon` | `\epsilon` | Small constant |
| `delta` | `\delta` | Perturbation |

## Notation Conventions

### Sets and Spaces
- Sets: calligraphic `\mathcal{S}`
- Probability: `p(\cdot)`, `\mathbb{E}[\cdot]`
- Spaces: `\mathbb{R}^d`

### Vectors and Matrices
- Vectors: bold lowercase `\mathbf{x}`
- Matrices: bold uppercase `\mathbf{W}`
- Scalars: italic `x`, `n`, `d`

### Operations
- Argmin/argmax: `\arg\min_{x}`, `\arg\max_{x}`
- Norm: `\|\mathbf{x}\|`, `\|\mathbf{x}\|_2`
- Inner product: `\langle \mathbf{a}, \mathbf{b} \rangle`
- Element-wise: `\odot` (Hadamard), `\otimes` (Kronecker)
- Concatenation: `[\mathbf{a}; \mathbf{b}]` or `\mathbf{a} \| \mathbf{b}`
- Assignment: `\leftarrow`
- Definition: `\triangleq` or `\coloneqq`

### Distributions
- Gaussian: `\mathcal{N}(\mu, \sigma^2)`
- Uniform: `\mathcal{U}(a, b)`
- Categorical: `\mathrm{Cat}(\boldsymbol{\pi})`

### Common Phrases
- "for each" → `\forall`
- "exists" → `\exists`
- "such that" → `\text{s.t.}`
- "independent and identically distributed" → `\mathrm{i.i.d.}`
- "with respect to" → `\mathrm{w.r.t.}`
