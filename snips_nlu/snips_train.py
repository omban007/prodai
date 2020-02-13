import io
import json
import datetime
import os
import shutil

from snips_nlu import SnipsNLUEngine

model_path = "snips_trained_model"


def train_nlu():
    with io.open("training_data/dataset.json") as f:
        sample_dataset = json.load(f)

    nlu_engine = SnipsNLUEngine()

    print("Snips training started")
    train_start = datetime.datetime.now()
    nlu_engine = nlu_engine.fit(sample_dataset)

    if os.path.exists(model_path):
        shutil.rmtree(model_path, ignore_errors=True)
        nlu_engine.persist(model_path)
    else:
        nlu_engine.persist(model_path)

    train_end = datetime.datetime.now()
    print("Total time to train the Snips model: {0}".format(train_end - train_start))


if __name__=="__main__":
    train_nlu()
