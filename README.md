# HR-Recruiter-Chatbot-with-Rasa
HR Recruiter Chatbot with Rasa

You should have Python3.6 and pip manager installed on your machine.

Here is how to install the dependencies

pip install -r requirements.txt

And then train the NLU model by,

python nlu_model.py

this will create a NLU model under models directory.

And then train the Dialogue model by,

python train_dialogue.py

Running Bot from command line

Run the command in terminal, and keep it running

python -m rasa_core_sdk.endpoint --actions actions

Start a new terminal and type the command,

python dialogue_management.py

And chat with with Recruitment bot.
Running Bot in Interactive mode

For Interactive training, Run the command in terminal, and keep it running

python -m rasa_core_sdk.endpoint --actions actions

Start a new terminal and type the command,

python train_dialogue.py

And dynamically create storyboard and training data for your bot.
