**Build Docker Container** 

`docker build -t llm-wrapper-api .`

**Run Docker Container**

`docker run -d --name fastapi-zero-shot -p 8000:8000 llm-wrapper-api`

Citation
If you use this model academically, please cite:

@misc{laurer_building_2023,
    title = {Building {Efficient} {Universal} {Classifiers} with {Natural} {Language} {Inference}},
    url = {http://arxiv.org/abs/2312.17543},
    doi = {10.48550/arXiv.2312.17543},
    abstract = {Generative Large Language Models (LLMs) have become the mainstream choice for fewshot and zeroshot learning thanks to the universality of text generation. Many users, however, do not need the broad capabilities of generative LLMs when they only want to automate a classification task. Smaller BERT-like models can also learn universal tasks, which allow them to do any text classification task without requiring fine-tuning (zeroshot classification) or to learn new tasks with only a few examples (fewshot), while being significantly more efficient than generative LLMs. This paper (1) explains how Natural Language Inference (NLI) can be used as a universal classification task that follows similar principles as instruction fine-tuning of generative LLMs, (2) provides a step-by-step guide with reusable Jupyter notebooks for building a universal classifier, and (3) shares the resulting universal classifier that is trained on 33 datasets with 389 diverse classes. Parts of the code we share has been used to train our older zeroshot classifiers that have been downloaded more than 55 million times via the Hugging Face Hub as of December 2023. Our new classifier improves zeroshot performance by 9.4\%.},
    urldate = {2024-01-05},
    publisher = {arXiv},
    author = {Laurer, Moritz and van Atteveldt, Wouter and Casas, Andreu and Welbers, Kasper},
    month = dec,
    year = {2023},
    note = {arXiv:2312.17543 [cs]},
    keywords = {Computer Science - Artificial Intelligence, Computer Science - Computation and Language},
}
