# When Vision-Language Models Look but Don't See: Anatomical Bias in Endoscopic Spatial Reasoning
<img src="figures/Pipeline.jpg" alt="Pipeline" width="700">

Welcome to the repository for our ISBI2026 paper, currently under peer review. Here, you'll find scripts, datasets, and models essential for our research. 🚀

📊 Data EndoSSS-RP
Summary: 

🔗 **Dataset:** For detailed information about file structure and contents, see [data.md](./data.md)

🔗 **Code:** [GitHub](https://github.com/DiegoBravoH/EndoNavQA.git)

This section provides an overview of the datasets used in our study 📌.
- 📊 Stomach Site Images: 387 patients.

📂 For more details: Check out the [data.md](data.md) file for a comprehensive guide on data organization and preprocessing steps.

## 🎯 Quantitative Results: Impact of Anatomical Bias
**Legend**

⊙ = Dot

◆ = Number

□ = Letter

### Original
| Method                     | Level 1     | Level 2                 | Level 3                 | AS                      |
| -------------------------- | ----------- | ----------------------- | ----------------------- | ----------------------- |
| **Gemini-2.5**             | 66.78 ±0.06 | 97.46<sup>⊙</sup> ±0.06 | 97.71<sup>□</sup> ±0.04 | 99.61<sup>⊙</sup> ±0.01 |
| **GPT-4o**                 | 68.08 ±0.32 | 76.39<sup>⊙</sup> ±0.59 | 86.89<sup>◆</sup> ±0.20 | 97.43<sup>◆</sup> ±0.36 |
| **GPT-4o (Q: right/left)** | 58.66 ±0.33 | 66.96<sup>⊙</sup> ±1.15 | 86.00<sup>◆</sup> ±0.52 | 97.35<sup>◆</sup> ±0.32 |
| **JanusPro-7B**            | 48.28 ±0.27 | 43.18<sup>⊙</sup> ±1.06 | 52.02<sup>⊙</sup> ±0.69 | 67.25<sup>⊙</sup> ±0.48 |
| **LLaMA-3.2**              | 51.02 ±0.36 | 52.97<sup>⊙</sup> ±1.64 | 53.63<sup>⊙</sup> ±0.70 | 55.22<sup>⊙</sup> ±0.07 |

### Flip
| Method                     | Level 1     | Level 2                 | Level 3                 | AS |
| -------------------------- | ----------- | ----------------------- | ----------------------- | -- |
| **Gemini-2.5**             | 58.04 ±0.09 | 97.71<sup>⊙</sup> ±0.09 | 98.06<sup>⊙</sup> ±0.04 | –  |
| **GPT-4o**                 | 61.48 ±0.01 | 68.06<sup>⊙</sup> ±0.26 | 87.43<sup>◆</sup> ±0.32 | –  |
| **GPT-4o (Q: right/left)** | 47.25 ±0.09 | 51.61<sup>⊙</sup> ±0.43 | 87.13<sup>◆</sup> ±0.03 | –  |
| **JanusPro-7B**            | 48.30 ±1.14 | 41.78<sup>⊙</sup> ±1.12 | 54.86<sup>⊙</sup> ±0.45 | –  |
| **LLaMA-3.2**              | 50.32 ±0.39 | 50.55<sup>⊙</sup> ±1.56 | 50.67<sup>□</sup> ±0.74 | –  |

### Rotation
| Method                     | Level 1     | Level 2                 | Level 3                 | AS |
| -------------------------- | ----------- | ----------------------- | ----------------------- | -- |
| **Gemini-2.5**             | 42.15 ±0.03 | 97.30<sup>⊙</sup> ±0.04 | 97.75<sup>⊙</sup> ±0.10 | –  |
| **GPT-4o**                 | 45.80 ±0.15 | 54.50<sup>⊙</sup> ±0.39 | 87.77<sup>⊙</sup> ±0.21 | –  |
| **GPT-4o (Q: right/left)** | 47.18 ±0.03 | 53.20<sup>⊙</sup> ±0.19 | 86.39<sup>◆</sup> ±0.03 | –  |
| **JanusPro-7B**            | 46.33 ±1.28 | 41.77<sup>⊙</sup> ±0.57 | 52.44<sup>⊙</sup> ±0.68 | –  |
| **LLaMA-3.2**              | 50.35 ±0.69 | 51.54<sup>⊙</sup> ±0.29 | 52.02<sup>⊙</sup> ±0.08 | –  |

Accuracy comparison across prompt levels and VLMs. Symbols indicate the best-performing marker type for each setting: $^{\odot}$ (Dot), $^{\diamond}$ (Number), and $^{\square}$ (Letter) in Levels 2–3 and in the Ablation Study (AS). “Q: right/left” denotes the variant using binary right/left questions, included for the best-performance comparison in Level 1.



**Figure:** Accuracy comparison across prompt levels and VLMs.  
Symbols indicate the best-performing marker type for each setting:  
$^{\odot}$ (*Dot*), $^{\diamond}$ (*Number*), and $^{\square}$ (*Letter*) in Levels 2–3 and the Ablation Study (AS, see Section \ref{sec:AS}).  
“General results” refer to mean accuracy across original, flipped, and rotated images for GPT-4o.


<img src="figures/Results.jpg" alt="Result" width="700">

**Figure:** Mean accuracy across VLMs for each prompt level (Levels 1–3) using original endoscopic images, and for the ablation study (AS) using marker-only phantom images without endoscopic content.


## 🔨 Installation
Please refer to the [libraries.md](libraries.md) file for detailed installation instructions.



