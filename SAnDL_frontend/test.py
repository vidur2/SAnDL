"""""
SLIDE 1: 
From crafting art to powering chatbots, Generative AI has revolutionized the way we interact with technology.
As its applications continue to expand, so does the need for responsible usage. 

SLIDE 2:
One way to prevent misuse is through anomaly detection, a process that flags potentially harmful behaviors.
While lots of security detection systems already employ anomaly detection
systems, there is a distinct lack of these systems for generative AI, especially in large language models. 

SLIDE 3/4: SANDL
This is where SAnDL comes into play. SAnDL stands for Sophisticated Anomaly 
Detection for Large Language Models and is a simple solution to this problem.

SLIDE 5: MODEL ARCHITECTURE
For our model, we used Sentence Transformers from Hugging Face to convert prompts into vector embeddings, which were fed into a series 
of isolation forests, using unsupervized learning to determine the likelihood that a prompt is not malicious.
Each isolation forest in the series has a varying value for contamination, which is the percent of the dataset that is anomalous. 
The likelihood is then determined by averaging the results of passing a prompt through these forests.

SLIDE 6: DESIGN ARCHITECTURE
Now let's take a look at how the model works.
When a user signs up or logs in through the frontend, the information is sent to the server, which then queries a PostgreSQL database
to verify it. the result of this is then passed back through the server to the frontend.

SLIDE 7: DESIGN ARCHITECTURE PT 2
Alternatively, when a user enters a prompt, it is sent to the server, which first checks it with the Redis cache,
where we use sklearn's tfidf vectorizer to convert the prompt to a vector, which is compared to cached vectors 
that were created for previous prompts. If these vectors are sufficiently similar, a cached probability for maliciousness is given.
Otherwise, the prompt returns to the server and is then sent to the model, producing a probability which is sent back to the 
server and then the frontend.

----DEMO








2:
Large language models in particular have little to no anomaly detection, 
making them susceptible to malicious engineering and attacks. 

When the user types in a prompt, the prompt is first sent to the Redis cache, where we use sklearn's tfidf vectorizer to
convert the prompt to a vector, which we can then compare to the cached vectors that were created for previous prompts. 
If the prompt is similar enough, then a cached probability for maliciousness is given. Otherwise, the prompt is sent to the
model to output a prediction, which is sent back to the server and then the frontend. 



SAnDL works by  ---- model image
______

To generate a percentage, note that isolation forest models require a 
contamination, which is the percent of the dataset that's anomalous. Using a variety of values for the contamination we average the
results over mutiple isolation forests to produce our percentage. 


**DEMO**
-- 


"""