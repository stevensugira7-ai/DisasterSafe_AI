# DisasterSafe AI — beginner prototype

This is a student prototype for a location-based natural-disaster awareness application.

## Important limitation
The current app uses simple example rules. It is NOT a trained AI model and does NOT connect to live weather, official alerts, maps, or evacuation routes. Do not use it for real emergency decisions.

## Run it on Windows

1. Install Python if it is not already installed.
2. Extract this ZIP file.
3. Open PowerShell in the extracted `disastersafe_ai` folder.
4. Install the dependency:

   `python -m pip install -r requirements.txt`

5. Start the app:

   `python -m streamlit run app.py`

6. Open the local address shown in PowerShell, usually `http://localhost:8501`.

If `python` is not recognized, try `py -m pip install -r requirements.txt` and `py -m streamlit run app.py`.

## Next development step
To make this a real AI project, obtain a reliable, relevant historical dataset, define the prediction target, train and evaluate a model, and only then connect it to the application. Add official warning and mapping integrations separately and validate all safety guidance with reliable sources.
