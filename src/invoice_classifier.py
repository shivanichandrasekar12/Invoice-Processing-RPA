import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

class InvoiceAI:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = RandomForestClassifier()
        # Mock training data representing different departments
        self.train_data = {
            'text': ['cloud server hosting azure', 'office cleaning sanitation', 'legal consultation fees', 'hardware laptop procurement'],
            'label': ['IT', 'Facilities', 'Legal', 'Procurement']
        }
        self._train()

    def _train(self):
        df = pd.DataFrame(self.train_data)
        X = self.vectorizer.fit_transform(df['text'])
        self.model.fit(X, df['label'])

    def predict_department(self, invoice_text):
        X_test = self.vectorizer.transform([invoice_text.lower()])
        prediction = self.model.predict(X_test)
        return prediction[0]
