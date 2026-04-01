<!-- hide -->
# Integration of a ML model in Render using Flask - Step by step guide
<!-- endhide -->

- Search and understand a new dataset.
- Model the data using a Machine Learning, Deep Learning or NLP algorithm.
- Analyze the results and optimize the model.
- Integrate it into Render using a Flask-based application.
  
## 🌱  How to start this project

Follow the instructions below:

1. Create a new repository based on [machine learning project](https://github.com/4GeeksAcademy/machine-learning-python-template/generate) by [clicking here](https://github.com/4GeeksAcademy/machine-learning-python-template).
2. Open the newly created repository in Codespace using the [Codespace button extension](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace-for-a-repository).
3. Once the Codespace VSCode has finished opening, start your project by following the instructions below.

## 🚛 How to deliver this project

Once you have finished solving the exercises, be sure to commit your changes, push to your repository and go to 4Geeks.com to upload the repository link.

## 📝 Instructions

### Step 1: Find a dataset

Research different online sources about different datasets that you could use to train a model. You can use some public API, the UCI repository for Machine Learning or the Kaggle section of [datasets](https://www.kaggle.com/datasets), among many other sources. Remember to look for a simple dataset as this is not the final project of the course.

### Step 2: Develop a model

Once you have found your ideal data set, analyze it and train a model. Optimize it if necessary.

### Step 3: Develop a web application using Flask

With the knowledge acquired in this module, develop an interface to be able to use the model. Give it the style that suits you best and note the external resources you have used for the development.

### Step 4: Integrate the model and the application in Render

Create a free service in Render and integrate the work you have done to be able to deploy the web application online. Don't forget to include the link to the service in your repository.

## Sample implementation in this repository

This repository now includes a complete Flask + ML example using the Iris dataset:

- `src/train_model.py`: trains and saves the model artifact.
- `model/iris_model.joblib`: serialized trained model.
- `app.py`: Flask app with `/` and `/predict` routes.
- `templates/index.html` and `static/styles.css`: user interface.
- `render.yaml`: Render deployment configuration.

### Run locally

1. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

2. Train the model (or retrain it):

```bash
python src/train_model.py
```

3. Start the Flask app:

```bash
python app.py
```

4. Open the app at `http://127.0.0.1:3000`.

### Deploy on Render

This repository includes `render.yaml` using:

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
