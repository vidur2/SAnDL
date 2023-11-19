# SAnDL
Welcome to **SAnDL**! 

SAnDL stands for Sophisticated Anomaly Detection for Large Language Models and is a webapp used for detecting anomalies in prompts given to large language models. Prompts can be enterred into SAnDL, outputting a percentage that represents the likelihood that the enterred prompt is non-malicious. Each user is also given an API key upon creation of an account.

## The Model
Our model uses [Sentence Transformers](https://huggingface.co/docs/transformers/model_doc/bert) from [Hugging Face](https://huggingface.co/) to convert prompts into vector embeddings. These vector embeddings were then fed into a series of isolation forests, where unsupervized learning was used to determine the likelihood that a prompt is not malicious. 

## Running the Front-end
SAnDL was created using the [Streamlit](https://streamlit.io/) framework for Python.

To run the front-end, run `streamlit run 3_Logout.py` while in the `SAnDL_frontend` directory.

### Contact Us
You can reach out to us on LinkedIn.
