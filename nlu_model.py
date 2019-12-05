from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config


def create_nlu(data_file="data/nlu_data.md",
               config_file="nlu_config.yml"):
    '''
    This function trains NLU model and persists the model
    :param data_file: data file for NLU
    :param config_file: config file for NLU
    :return:
    '''
    # loading the nlu training samples
    training_data = load_data(data_file)

    # trainer to educate our pipeline
    trainer = Trainer(config.load(config_file))

    # train the model!
    interpreter = trainer.train(training_data)

    # store it for future use
    model_directory = trainer.persist("./models/nlu", fixed_model_name="current")

    return interpreter, model_directory

if __name__ == '__main__':
    create_nlu()
