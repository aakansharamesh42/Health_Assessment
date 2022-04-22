import pickle


with open('diabetes.pkl', 'rb') as f:
    data = pickle.load(f)

print(data)