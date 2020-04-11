Here is our plan of action:

    We will classify text using Deep Learning
    We will practice by building a classification model trained in news articles from the BBC.
    We will test the model on news headlines we will scrape from Google Trends.
    We will build a similar model but we will train it on a different dataset with questions grouped by their intention.
    We will use Google Data Studio to pull potential questions from Google Search Console.
    We will use the model to classify the questions we export from Data Studio.
    We will group the questions by their intention and extract actionable insights we can use to prioritize content development efforts.
    We will go over the underlying concepts that make this possible: word vectors, embeddings, and encoders/decoders.
    We will build a sophisticated model that can parse not just intent but also specific actions like the ones we give to Siri and Alexa.

In reference of issue no #57
Uber Ludwig

Completing the plan I described in issue #57 using Deep Learning generally requires writing advanced Python code. Fortunately, Uber has released a super valuable tool called Ludwig that makes it possible to build and use predictive models with incredible ease. We will run Ludwig from within Google Colaboratory in order to use their free GPU runtime. Training Deep Learning models without using GPUs can be the difference between waiting a few minutes to waiting hours.
Automated Text Classification

In order to build predictive models, we need relevant labeled data and moded definitions. So, you will practice with a simple text classification model straight from the Ludwig examples. We are going to use a labeled dataset of BBC articles organized by category. This article should give you a sense of the level of coding we won’t have to do because we are using Ludwig.
