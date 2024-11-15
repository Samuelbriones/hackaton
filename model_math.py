# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_squared_error, r2_score

# # Cargar los datos
# df = pd.read_csv('/home/crowstar/Escritorio/Programación/Hackaton/backend/data.csv')

# # Vista previa de los datos
# print(df.head())

# # Comprobar valores nulos
# print(df.isnull().sum())

# features = [
#     'Access to electricity (% of population)',
#     'Access to clean fuels for cooking',
#     'Electricity from fossil fuels (TWh)',
#     'Electricity from renewables (TWh)',
#     'Electricity from nuclear (TWh)',
#     'Primary energy consumption per capita (kWh/person)',
# ]

# target = 'Value_co2_emissions_kt_by_country'


# df = df[features + [target]].dropna()

# X = df[features]
# y = df[target]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Crear el modelo
# model = RandomForestRegressor(n_estimators=100, random_state=42)

# # Entrenar el modelo
# model.fit(X_train, y_train)

# # Predicciones
# y_pred = model.predict(X_test)

# # Evaluación
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# print(f'Mean Squared Error (MSE): {mse}')
# print(f'R² Score: {r2}')

# import joblib

# # Guardar el modelo entrenado
# joblib.dump(model, 'co2_model.pkl')

# print("Modelo guardado exitosamente.")

# # Cargar el modelo guardado
# loaded_model = joblib.load('co2_model.pkl')

# # Usar el modelo cargado para hacer predicciones
# y_pred_loaded = loaded_model.predict(X_test)
# print("Predicciones con el modelo cargado:", y_pred_loaded)
