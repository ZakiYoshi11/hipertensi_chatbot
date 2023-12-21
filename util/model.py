import numpy as np

class MultinomialNaiveBayes:
    def __init__(self):
        self.classes = None
        self.prior_probs = None
        self.likelihood_probs = None

    # Menghitung Probabilitas Class pada data yang ada
    def calculate_prior_probability(self, y):
        classes, class_counts = np.unique(y, return_counts=True)
        prior_probs = {}
        total_instances = len(y)
        for class_label, class_count in zip(classes, class_counts):
            prior_probs[class_label] = class_count / total_instances
        return prior_probs
    #  Menghitung fitur pada setiap kelas dan ditambahkan 1 agar hasil tidak 0
    def calculate_likelihood(self, X, y):
        classes, class_counts = np.unique(y, return_counts=True)
        likelihood_probs = {}
        num_features = X.shape[1]
        for class_label, class_counts in zip(classes, class_counts):
            class_instances = X[y == class_label]
            feature_counts = np.sum(class_instances, axis=0)
            total_counts = np.sum(feature_counts)
            likelihood_probs[class_label] = (feature_counts + 1) / (total_counts + num_features)
        return likelihood_probs
        
    def fit(self, X, y):
        self.classes = np.unique(y)
        self.prior_probs = self.calculate_prior_probability(y)
        self.likelihood_probs = self.calculate_likelihood(X, y)

    # Melakukan proses prediksi dengan melakukan perhitungan berdasarkan hasil dari prior prob dan
    # likehood prob  untuk menampilkan class yang memiliki probabilitas tertinggi
    def predict_class(self, X):
        predictions = []
        for instance in X:
            instance_probs = []
            for class_label in self.classes:
                class_prob = np.log(self.prior_probs[class_label])
                likelihood_probs = self.likelihood_probs[class_label]
                instance_prob = np.sum(np.log(likelihood_probs) * instance)
                instance_probs.append(class_prob + instance_prob)
                
            # Transform log-probabilities to probabilities using softmax
            instance_probs = np.array(instance_probs)
            exp_probs = np.exp(instance_probs - np.max(instance_probs)) 
            softmax_probs = exp_probs / np.sum(exp_probs)
            predicted_class = self.classes[np.argmax(softmax_probs)]
            predictions.append(predicted_class)
        return predictions
    
    # Melakukan proses prediksi dengan melakukan perhitungan berdasarkan hasil dari prior prob dan
    # likehood prob  untuk menampilkan probabilitas dari class yang di prediksi
    def predict_prob (self, X):
        pred_probs = []
        for instance in X:
            instance_probs = []
            for class_label in self.classes:
                class_prob = np.log(self.prior_probs[class_label])
                likelihood_probs = self.likelihood_probs[class_label]
                instance_prob = np.sum(np.log(likelihood_probs) * instance)
                instance_probs.append(class_prob + instance_prob)
                
            # Transform log-probabilities to probabilities using softmax
            instance_probs = np.array(instance_probs)
            exp_probs = np.exp(instance_probs - np.max(instance_probs)) 
            softmax_probs = exp_probs / np.sum(exp_probs)
            pred_probs.append(max(softmax_probs))
        return pred_probs
    
