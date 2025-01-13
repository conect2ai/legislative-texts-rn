&nbsp;
&nbsp;
<p align="center">
  <img width="800" src="./images/conecta_logo.png" />
</p>

&nbsp;

# Exploring Legislative Texts in Brazilian Portuguese: Readability Analysis and Knowledge Graph Generation Using Llama 3.2

### ✍🏾 Authors: [Gisliany Alves](https://github.com/gisliany), [Breno Santana Santos](https://github.com/breno-madruga), [Marianne Diniz](https://github.com/MarianneDiniz), [Ivanovitch Silva](https://github.com/ivanovitchm)

## 1. Abstract/Overview

Legislative documents are fundamental pillars of democratic societies, defining citizens' rights and responsibilities while establishing laws and regulations that govern societal interactions. However, as these documents usually show some textual complexity, they become incomprehensible to the general public. Furthermore, research in the legislative domain in Brazilian Portuguese remains underexplored, with a notable scarcity of resources, such as models and datasets tailored to the legal field. To address these issues, a data-oriented methodology supported by Large Language Models (LLMs) was proposed for analyzing legislative documents and extracting Knowledge Graphs (KGs) from their content. To validate this approach, a case study was performed using a corpus provided by the Legislative Assembly of Rio Grande do Norte (ALRN), Brazil, which comprises 1,869 proposals from January 2019 to April 2024. In addition, the Llama 3.2 3B Instruct model was employed for this empirical evaluation to extract KGs, representing entities and relationships within the texts. The results suggest the feasibility of the proposed methodology, demonstrating its suitability to generate coherent graphs aligned with the source material. However, limitations were observed in the entity disambiguation and relationship completeness tasks performed by the chosen model. Moreover, from the ALRN's proposals corpus, its readability was assessed using some indicators for the Brazilian Portuguese language, revealing that the texts demand advanced reading skills due to their technical nature. Finally, this work contributes to Legal Artificial Intelligence by offering insights from Brazilian legislative texts and highlights opportunities for improving legislative transparency and accessibility through advanced natural language processing techniques.

## 2. Artifacts

The results can be found in the notebook:
📕 #01 Analyzing Legislative Data

The remainder of this repository holds the folders:
- `data`: This folder serves as the destination for downloading the dataset used in the project. It also contains an intermediate dataset that includes readability metrics.
- `images`: Stores visual assets related to the project, such as figures generated during analysis or for documentation purposes.
- `models`: This folder is where Llama 3.2 3B Instruct will be downloaded
- `utils`: Contains utility scripts or helper functions used throughout the project, such as data preprocessing scripts and reusable code.

## 3. Environment Setup

### Requirements
1. Python 3.12
2. Miniconda 23.11 or greater
3. [Visual Studio Code](https://code.visualstudio.com/)

### Setup

1. Clone this repository:

```bash
git clone https://github.com/conect2ai/legislative-texts-rn.git
```
  
2. Create a file named `.env` based on `.env_template`. `BASE_DIR` specifies the absolute path to the project folder (filled with it), while `HUGGING_FACE_TOKEN` is the token used to authenticate and download the required model. You can generate your token from your [Hugging Face](https://huggingface.co/settings/tokens) account Settings > Access Token.
   
3. Create your conda environment named `legislative` executing:

```bash
conda env create -f environment.yml
```

4. Activate the environment using `conda activate legislative`. Now, you can run the notebook in it.

## 4. Additional Notes

- Hugging Face Token Permissions:
Ensure your Hugging Face token has the appropriate permission (READ) to download the model.

- Variability of the Generated Knowledge Graph (KG):
Even when setting a random seed, the generated Knowledge Graph (KG) may vary slightly due to factors beyond direct control. Some potential reasons include:

  - Non-Deterministic Operations: Certain GPU operations, such as matrix multiplications or cumulative sums, may use non-deterministic algorithms depending on your hardware and software configuration.
  - CUDA and CuBLAS Behavior: GPU operations often rely on CuBLAS, which can introduce slight variations in computation.
  - Floating-Point Precision: The inherent nature of floating-point arithmetic on GPUs may produce slightly different results on different hardware or configurations.

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# About us

The research group [**Conect2AI**](http://conect2ai.dca.ufrn.br) consists of undergraduate and graduate students from the Federal University of Rio Grande do Norte (UFRN) and aims to apply Artificial Intelligence (AI) and machine learning in emerging fields. Our expertise includes Embedded Intelligence and IoT, optimizing resource management and energy efficiency, contributing to sustainable cities. In energy transition and mobility, we apply AI to optimize energy use in connected vehicles and promote more sustainable mobility.
