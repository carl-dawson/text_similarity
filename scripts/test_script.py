import requests
import json


if __name__ == '__main__':
    """
    test the text_similarity API with the three sample texts
    """

    url = "http://0.0.0.0:3333/compare_texts"

    with open('sample_1.txt', 'r') as f:
        sample_1 = f.read()

    with open('sample_2.txt', 'r') as f:
        sample_2 = f.read()

    with open('sample_3.txt', 'r') as f:
        sample_3 = f.read()

    data = json.dumps([sample_1, sample_2])
    r = requests.post(url, data=data)
    similarity_score = r.json()
    print(f"Sample 1 | Sample 2 : {similarity_score:.4f}")

    data = json.dumps([sample_1, sample_3])
    r = requests.post(url, data=data)
    similarity_score = r.json()
    print(f"Sample 1 | Sample 3 : {similarity_score:.4f}")

    data = json.dumps([sample_2, sample_3])
    r = requests.post(url, data=data)
    similarity_score = r.json()
    print(f"Sample 2 | Sample 3 : {similarity_score:.4f}")