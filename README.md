# A Benchmark and Evaluation Framework for Visual Spatial Reasoning in UGI Endoscopy
<img src="figures/Pipeline.jpg" alt="Pipeline" width="700">

Welcome to the repository for our ISBI2026 paper, currently under peer review. Here, you'll find scripts, datasets, and models essential for our research. 🚀

📊 Data EndoSSS-RP
Summary: 
🔗 **Dataset:** [Figshare](https://doi.org/10.6084/m9.figshare.27308133)
🔗 **Code:** [GitHub](https://github.com/DiegoBravoH/EndoNavQA.git)

This section provides an overview of the datasets used in our study 📌.
- 📊 Stomach Site Images: 387 patients.

📂 For more details: Check out the [data.md](data.md) file for a comprehensive guide on data organization and preprocessing steps.

## 🎯 Quantitative Results: Impact of Anatomical Bias

| Condition | Method | Level 1 | Level 2 | Level 3 | AS |
|:-----------|:--------|:-------:|:-------:|:-------:|:---:|
| **Original** | GPT-4o | 68.08 ± 0.32 | 76.39 ± 0.59 ⊙ | 86.89 ± 0.20 ◇ | 97.43 ± 0.36 ◇ |
|  | GPT-4o (Q: right/left) | 58.66 ± 0.33 | 66.96 ± 1.15 ⊙ | 86.00 ± 0.52 ◇ | 97.35 ± 0.32 ◇ |
|  | JanusPro-7B | 48.28 ± 0.27 | 43.18 ± 1.06 ⊙ | 52.02 ± 0.69 ⊙ | 67.25 ± 0.48 ⊙ |
|  | LLaMA 3.2 | 51.02 ± 0.36 | 52.97 ± 1.64 ⊙ | 53.63 ± 0.70 ⊙ | 55.22 ± 0.07 ⊙ |
| **Flip** | GPT-4o | 61.48 ± 0.01 | 68.06 ± 0.26 ⊙ | 87.43 ± 0.32 ◇ | – |
|  | GPT-4o (Q: right/left) | 47.25 ± 0.09 | 51.61 ± 0.43 ⊙ | 87.13 ± 0.03 ◇ | – |
|  | JanusPro-7B | 48.30 ± 1.14 | 41.78 ± 1.12 ⊙ | 54.86 ± 0.45 ⊙ | – |
|  | LLaMA 3.2 | 50.32 ± 0.39 | 50.55 ± 1.56 ⊙ | 50.67 ± 0.74 □ | – |
| **Rotation** | GPT-4o | 45.80 ± 0.15 | 54.50 ± 0.39 ⊙ | 87.77 ± 0.21 ⊙ | – |
|  | GPT-4o (Q: right/left) | 47.18 ± 0.03 | 53.20 ± 0.19 ⊙ | 86.39 ± 0.03 ◇ | – |
|  | JanusPro-7B | 46.33 ± 1.28 | 41.77 ± 0.57 ⊙ | 52.44 ± 0.68 ⊙ | – |
|  | LLaMA 3.2 | 50.35 ± 0.69 | 51.54 ± 0.29 ⊙ | 52.02 ± 0.08 ⊙ | – |
| **General results** | GPT-4o (Q: Overall) | 58.46 ± 11.44 | 66.31 ± 11.03 ⊙ | 87.19 ± 0.27 ◇ | 97.43 ± 0.36 ◇ |
|  | GPT-4o (Q: right/left) | 51.03 ± 6.61 | 57.26 ± 8.44 ⊙ | 86.09 ± 1.01 ◇ | 97.35 ± 0.32 ◇ |
|  | GPT-4o (Q: above/below) | 67.56 ± 20.01 | 77.17 ± 18.54 ⊙ | 88.35 ± 0.80 ◇ | 97.53 ± 0.42 ◇ |

**Figure:** Accuracy comparison across prompt levels and VLMs.  
Symbols indicate the best-performing marker type for each setting:  
$^{\odot}$ (*Dot*), $^{\diamond}$ (*Number*), and $^{\square}$ (*Letter*) in Levels 2–3 and the Ablation Study (AS, see Section \ref{sec:AS}).  
“General results” refer to mean accuracy across original, flipped, and rotated images for GPT-4o.


<img src="figures/Results.jpg" alt="Result" width="700">

**Figure:** Mean accuracy across VLMs for each prompt level (Levels 1–3) using original endoscopic images, and for the ablation study (AS) using marker-only phantom images without endoscopic content.


## 🔨 Installation
Please refer to the [libraries.md](libraries.md) file for detailed installation instructions.



