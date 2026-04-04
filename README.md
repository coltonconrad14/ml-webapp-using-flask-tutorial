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

This repository now includes both **Flask** and **Streamlit** versions of the Iris ML app:

- `src/train_model.py`: trains and saves the model artifact.
- `model/iris_model.joblib`: serialized trained model.
- `app.py`: Flask app with `/` and `/predict` routes.
- `streamlit_app.py`: Streamlit version ready for Render deployment.
- `src/predictor.py`: shared model loading and prediction helpers.
- `templates/index.html` and `static/styles.css`: Flask user interface.
- `render.yaml`: Render deployment configuration for both services.

### Run locally

1. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

2. Train the model (or retrain it):

```bash
python src/train_model.py
```

3. Start the Streamlit app:

```bash
python -m streamlit run streamlit_app.py
```

4. Or start the Flask app:

```bash
python app.py
```

### Deploy on Render

This repository includes `render.yaml` with:

- **Streamlit service:** `python -m streamlit run streamlit_app.py --server.address 0.0.0.0 --server.port $PORT`
- **Flask service:** `gunicorn --bind 0.0.0.0:$PORT app:app`

If you only want the Streamlit deployment, keep the `streamlit-iris-predictor` service in `render.yaml`.
