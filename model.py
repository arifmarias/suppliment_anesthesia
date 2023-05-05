import pandas as pd
from pycaret.classification import *
df = pd.read_csv("Data/Pulp Sensibility.csv")
df.head()
s = setup(data = df, target = 'Need Supliment', session_id=123)
best_model = compare_models(sort="F1")
et = create_model('et')
tuned_et = tune_model(et, optimize = 'F1')
final_et = finalize_model(tuned_et)
save_model(final_et,'Final_Model_05May2023')
