import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd

from src.model import simulated_model_response
from src.evaluator import evaluate_elite
from data.cases import cases

st.title("🧠 MedReasonBench Demo")

results = []

for case in cases:
    pred = simulated_model_response(case)
    score = evaluate_elite(pred, case["answer"])
    
    results.append({
        "Case": case["patient_id"],
        "Score": score,
        "Prediction": pred
    })

df = pd.DataFrame(results)

st.dataframe(df)

st.bar_chart(df.set_index("Case")["Score"])
