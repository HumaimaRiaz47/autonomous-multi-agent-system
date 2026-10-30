---
base_model: meta-llama/Llama-3.2-3B
library_name: transformers
model_name: price-2026-10-29_19.59.38-lite
tags:
- generated_from_trainer
- trl
- sft
licence: license
---

# Model Card for price-2026-10-29_19.59.38-lite

This model is a fine-tuned version of [meta-llama/Llama-3.2-3B](https://huggingface.co/meta-llama/Llama-3.2-3B).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "If you had a time machine, but could only go to the past or the future once and never return, which would you choose and why?"
generator = pipeline("text-generation", model="riazhumaima/price-2026-10-29_19.59.38-lite", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="150" height="24"/>](https://forge.coreweave.com/wandb/riazhumaima-udemy/price/runs/huu1mvk5) 



This model was trained with SFT.

### Framework versions

- TRL: 0.29.1
- Transformers: 5.21.0
- Pytorch: 2.14.1+cu130
- Datasets: 3.6.0
- Tokenizers: 0.23.3

## Citations



Cite TRL as:
    
```bibtex
@software{vonwerra2020trl,
  title   = {{TRL: Transformers Reinforcement Learning}},
  author  = {von Werra, Leandro and Belkada, Younes and Tunstall, Lewis and Beeching, Edward and Thrush, Tristan and Lambert, Nathan and Huang, Shengyi and Rasul, Kashif and GallouÃ©dec, Quentin},
  license = {Apache-2.0},
  url     = {https://github.com/huggingface/trl},
  year    = {2020}
}
```