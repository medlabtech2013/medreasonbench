def simulated_model_response(case):
    
    if case["patient_id"] == 1:
        return "Diagnosis: Anemia\nReasoning: Low hemoglobin\nConfidence: 0.85"
    
    elif case["patient_id"] == 2:
        return "Diagnosis: Diabetes\nReasoning: High glucose\nConfidence: 0.9"
    
    else:
        return "Diagnosis: Infection\nReasoning: Misinterpretation\nConfidence: 0.9"
