# BabyLM-Tiny

A comprehensive repository for the [BabyLM Challenge](https://babylm.github.io/) focused on efficient language model pretraining with limited data (1M words). This repository provides data sampling pipelines, model training templates, and evaluation scripts for BLiMP and GLUE benchmarks. Created by Nikita Goryeti and Moritz Ladenburger with assistance from Lukas Edman.

## Repository Structure

```
BabyLM-Tiny/
├── data/                          # Core training data (1M words)
│   ├── train.txt                  # Main training corpus
│   ├── dev.txt                    # Development set
│   └── tokenizer.model/.vocab     # Pre-trained tokenizer
├── datasets/                      # Extended datasets and sampling results
│   ├── BabyLM_dataset/           # Multi-domain corpora (100M→1M sampling)
│   ├── gutenberg/                # Project Gutenberg books by genre
│   ├── wiki_categories/          # Wikipedia articles by topic
│   └── open_subtitles/           # Movie subtitles by genre
├── sampling_pipelines/           # Data curation and sampling notebooks
│   ├── sample_babyLM_100M.ipynb       # Core multi-domain sampling
│   ├── sample_proj_gutenberg_books.ipynb # Literary genre datasets
│   ├── sample_wikipedia.ipynb          # Wikipedia topic sampling
│   └── sampling_subtitles.ipynb        # Movie subtitle datasets
├── trained_models/               # Model checkpoints and results
├── evaluation_data/              # BLiMP and GLUE evaluation sets
├── models_evaluation_results/    # Benchmark results and analysis
├── pipeline_template.ipynb       # Training pipeline template
└── evaluate_*.py                 # Evaluation scripts
```

## Setup

### Environment Configuration
1. **Copy the environment template:**
   ```bash
   cp .env.template .env
   ```

2. **Configure your credentials in `.env`:**
   ```bash
   # Required for GitHub operations
   GITHUB_TOKEN=your_github_personal_access_token
   
   # Required for movie subtitle sampling
   TMDB_API_KEY=your_tmdb_api_key
   
   # Required for model uploads
   HF_USERNAME=your_huggingface_username
   
   # Required for git operations
   GIT_USER_NAME="Your Name"
   GIT_USER_EMAIL=your.email@example.com
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Quick Start

### 1. Data Sampling
Use the sampling pipelines to create custom datasets:

```python
# Multi-domain balanced sampling (1M words)
from sampling_pipelines.sample_babyLM_100M import sample_proportions
sample_proportions("mixed_1M", 1_000_000, 
                  bnc_spoken=0.2, childes=0.2, gutenberg=0.2, 
                  open_subtitles=0.2, simple_wiki=0.2)

# Genre-specific literature sampling
sample_percentage_of_books(0.5, 1_000_000, "gutenberg_50pct")
```

### 2. Model Training
Use the training pipeline template:

```bash
# Open the training notebook
jupyter notebook pipeline_template.ipynb

# Or use specific model pipelines
jupyter notebook pipeline_deberta-v3-small.ipynb
```

### 3. Model Evaluation

**BLiMP Evaluation** (Linguistic acceptability):
```bash
python evaluate_blimp.py \
    --model_type [encoder/decoder] \
    --batch_size 64
```

**GLUE Evaluation** (Language understanding):
```bash
python evaluate_glue.py \
    --model_type [encoder/decoder] \
    --subset [cola/sst2/mrpc/qnli/rte/boolq/multirc] \
    --batch_size 64 \
    --learning_rate 5e-5 \
    --max_epochs 10 \
    --patience 3
```

## Key Features

### Data Sampling Pipelines
- **Multi-domain sampling**: Balanced mixing from 6 text types (spoken, child language, literature, subtitles, Wikipedia, phone conversations)
- **Genre-specific datasets**: Literature by genre (mystery, romance, sci-fi), Wikipedia by topic, movie subtitles by genre
- **Quantifier analysis**: Linguistic diversity analysis across different text types

### Training Infrastructure  
- **Model templates**: Ready-to-use training pipelines for DeBERTa, GPT, and other architectures
- **Tokenizer**: Pre-trained BPE tokenizer optimized for the 1M-word corpus
- **Environment setup**: Automated dependency management and GPU configuration

### Evaluation Framework
- **BLiMP**: 67 linguistic phenomena tests (syntax, semantics, morphology)
- **GLUE subset**: 7 fast tasks for language understanding
- **Automated reporting**: Results logging and comparison across models

## Usage Examples

### Custom Data Creation
```python
# Create domain-specific dataset
create_dataset_from_category("History", "wiki_history", 1_000_000)

# Sample books by percentage
sample_percentage_of_books(0.75, 1_000_000, "gutenberg_75pct")

# Generate movie genre datasets
process_genre_subtitles("Action", 1_000_000)
```

### Model Training
```python
# Basic training setup
model = AutoModelForMaskedLM.from_config(config)
trainer = SFTTrainer(model=model, train_dataset=dataset, ...)
trainer.train()
```

### Performance Analysis
- Models trained on different data types show varying performance on linguistic tasks
- Old English drama/poetry yields superior quantifier understanding despite lower variety
- Genre-specific training can improve domain-relevant capabilities

## Requirements

- Python 3.8+
- PyTorch
- Transformers
- Datasets
- Jupyter Notebook
- Additional dependencies in `requirements.txt`

