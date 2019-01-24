vectorizer.fit(data_train)

joblib.dump(random_forest, './models/random_forest.pkl')