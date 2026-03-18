def evaluate_elite(prediction, correct_answer):
    score = 0
    
    pred_lower = prediction.lower()
    correct_lower = correct_answer.lower()
    
    if correct_lower in pred_lower:
        score += 2
    else:
        score -= 1
        
    if "reason" in pred_lower:
        score += 1
        
    if "confidence" in pred_lower:
        score += 1
        
    if correct_lower not in pred_lower and "confidence" in pred_lower:
        score -= 2
        
    return score
