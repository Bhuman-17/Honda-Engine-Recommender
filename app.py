from flask import Flask, render_template, request
import pandas as pd
import joblib
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load data and models
df = pd.read_csv("Honda Engine Dataset.csv")
cat_cols = ["Product Type", "Shaft Rotation", "Fuel Type", "Charging System", "Engine Type"]
df[cat_cols] = df[cat_cols].astype(str).fillna("")

series_model = joblib.load("models/series_classifier_model.joblib")
reg_model = joblib.load("models/best_regressor_model.joblib")
le_series = joblib.load("models/series_label_encoder.joblib")

input_cols = cat_cols + ["Engine Displacement (cc)", "Maximum Power (HP)"]
output_regs = [
    "Bore (mm)", "Stroke (mm)", "Oil Capacity (L)",
    "Cylinders (qty.)", "Dry Weight (kg)", "Shaft Diameter (mm)"
]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/recommender')
def recommender():
    options = {col: sorted(df[col].dropna().unique()) for col in cat_cols}
    displacements = sorted(df["Engine Displacement (cc)"].dropna().unique())
    powers = sorted(df["Maximum Power (HP)"].dropna().unique())
    return render_template(
        "recommender.html",
        options=options,
        displacements=displacements,
        powers=powers
    )

@app.route('/dashboard')                                         
def dashboard():                                                   
    return render_template("dashboard.html")                       


@app.route('/results', methods=["POST"])
def results():
    form = request.form
    input_data = {
        "Product Type": form["product_type"],
        "Shaft Rotation": form["shaft_rotation"],
        "Fuel Type": form["fuel_type"],
        "Charging System": form["charging_system"],
        "Engine Type": form["engine_type"],
        "Engine Displacement (cc)": float(form["displacement"]),
        "Maximum Power (HP)": float(form["power"])
    }

    sample_input = pd.DataFrame([input_data])

    # Hard filter on categorical
    filtered = df.copy()
    for col in cat_cols:
        filtered = filtered[filtered[col] == sample_input.at[0, col]]

    if filtered.empty:
        return render_template("results.html", error="No engine matches the given categorical filters.")

    # Euclidean distance on numerical
    num_cols = ["Engine Displacement (cc)", "Maximum Power (HP)"]
    scaler = StandardScaler()
    X_filtered = scaler.fit_transform(filtered[num_cols])
    X_sample = scaler.transform(sample_input[num_cols])
    distances = euclidean_distances(X_filtered, X_sample).flatten()
    filtered["Distance"] = distances
    top3 = filtered.sort_values("Distance").head(3)

    predicted_series = le_series.inverse_transform(series_model.predict(sample_input))[0]
    predicted_specs = reg_model.predict(sample_input)[0]
    predicted_specs = {k: f"{v:.2f}" for k, v in zip(output_regs, predicted_specs)}

    return render_template(
        "results.html",
        input_data=input_data,
        top3=top3[input_cols + output_regs].to_dict(orient="records"),
        predicted_series=predicted_series,
        predicted_specs=predicted_specs
    )

@app.route('/why_choose')
def why_choose():
    return render_template("why_choose.html")

if __name__ == "__main__":
    app.run(debug=True)
