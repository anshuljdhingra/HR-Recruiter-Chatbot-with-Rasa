from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.train import interactive
from rasa_core.utils import EndpointConfig



def run_bot_online(interpreter,
                   domain_file="domain.yml",
                   training_data_file='data/stories.md'):
    '''
    This function trains the bot in an interactive manner
    :param interpreter: NLU Interpreter
    :param domain_file: Domain file
    :param training_data_file: Chat story board file
    :return: Agent
    '''

    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")

    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=3), KerasPolicy(max_history=5, epochs=300, batch_size=50)],
                  interpreter=interpreter,
                  action_endpoint=action_endpoint)

    data = agent.load_data(training_data_file)
    agent.train(data)
    interactive.run_interactive_learning(agent, training_data_file)
    return agent


if __name__ == '__main__':
    nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/current')
    run_bot_online(nlu_interpreter)