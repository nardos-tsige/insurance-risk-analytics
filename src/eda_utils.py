def calculate_loss_ratio(df): 
    df['LossRatio'] = df['TotalClaims'] / df['TotalPremium'] 
    df['Margin'] = df['TotalPremium'] - df['TotalClaims'] 
    df['HasClaim'] = (df['TotalClaims'] 
    return df 
