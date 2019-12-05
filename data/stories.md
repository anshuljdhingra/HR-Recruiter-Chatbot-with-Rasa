## Generated Story -250213808576262517
* greet
    - utter_greet
* position
    - utter_role
* position{"role_type": "technical"}
    - slot{"role_type": "technical"}
    - action_check_positions
    - slot{"positions": ["machine learning engineer", "ML product success engineer"]}
    - utter_knowmore
* affirm
    - utter_utilities
* position
    - utter_role
* position{"role_type": "business"}
    - slot{"role_type": "business"}
    - action_check_positions
    - slot{"positions": []}
    - utter_knowmore
* deny{"deny": "nope"}
    - utter_nothanks
    - utter_goodbye

## Generated Story -3368624641661029936
* greet
    - utter_greet
* position
    - utter_role
* position{"role_type": "business"}
    - slot{"role_type": "business"}
    - action_check_positions
    - slot{"positions": []}
    - utter_knowmore
* deny
    - utter_nothanks
    - utter_goodbye

## Generated Story 2565143873267614184
* greet
    - utter_greet
* position
    - utter_role
* position{"role_type": "any"}
    - slot{"role_type": "any"}
    - action_check_positions
    - slot{"positions": ["machine learning engineer", "ML product success engineer"]}
    - utter_knowmore

## Generated Story 1467969841943024158
* greet
    - utter_greet
* position
    - utter_role
* position{"role_type": "technical"}
    - slot{"role_type": "technical"}
    - action_check_positions
    - slot{"positions": ["machine learning engineer", "ML product success engineer"]}
    - utter_knowmore
* affirm
    - utter_utilities
* position
    - utter_role
* position{"role_type": "technical"}
    - slot{"role_type": "technical"}
    - action_check_positions
    - slot{"positions": ["machine learning engineer", "ML product success engineer"]}
    - utter_knowmore
* affirm{"affirm": "ya"}
    - utter_utilities
* position
    - utter_role
* position{"role_type": "business"}
    - slot{"role_type": "business"}
    - action_check_positions
    - slot{"positions": []}
    - utter_knowmore
* affirm
    - utter_utilities
* position
    - utter_role
* position{"role_type": "any"}
    - slot{"role_type": "any"}
    - action_check_positions
    - slot{"positions": ["machine learning engineer", "ML product success engineer"]}
    - utter_knowmore
* deny
    - utter_nothanks
    - utter_goodbye

## Generated Story -4339520876749317291
* greet+position
    - utter_simple_greet
    - utter_role
* position{"role_type": "technical"}
    - slot{"role_type": "technical"}
    - action_check_positions
    - slot{"positions": ["machine learning engineer", "ML product success engineer"]}
    - utter_knowmore
* affirm
    - utter_utilities
* position
    - utter_role
* position{"role_type": "business"}
    - slot{"role_type": "business"}
    - action_check_positions
    - slot{"positions": []}
    - utter_knowmore
* deny
    - utter_nothanks
    - utter_goodbye

## Generated Story -5033936019592687250
* greet+name+status{"PERSON": "Ali Park"}
    - slot{"PERSON": "Ali Park"}
    - utter_check
    - action_check_status
    - slot{"status": "rejected"}
    - utter_knowmore
* affirm
    - utter_utilities

## Generated Story -8350538276504998342
* greet+name+status{"PERSON": "jibin"}
    - slot{"PERSON": "jibin"}
    - utter_check
    - action_check_status
    - slot{"status": "unknown"}
    - utter_knowmore
* deny
    - utter_nothanks
    - utter_goodbye

## Generated Story -7797259046933396668
* greet+name+status{"PERSON": "Ali Park"}
    - slot{"PERSON": "Ali Park"}
    - utter_check
    - action_check_status
    - slot{"status": "interview"}
    - utter_knowmore
* affirm{"affirm": "y"}
    - utter_utilities
* position
    - utter_role
* position{"role_type": "technical"}
    - slot{"role_type": "technical"}
    - action_check_positions
    - slot{"positions": ["machine learning engineer", "ML product success engineer"]}
    - utter_knowmore
* affirm
    - utter_utilities

## Generated Story -8345141729428938342
* status
    - utter_name
* name{"PERSON": "Jibin"}
    - slot{"PERSON": "Jibin"}
    - utter_check
    - action_check_status
    - slot{"status": "received"}
    - utter_knowmore
* deny{"deny": "n"}
    - utter_nothanks
    - utter_goodbye

## Generated Story -1822903569460913038
* greet
    - utter_greet
* status
    - utter_name
* name{"PERSON": "Jibin"}
    - slot{"PERSON": "Jibin"}
    - utter_check
    - action_check_status
    - slot{"status": "unknown"}
    - utter_knowmore
* affirm
    - utter_utilities
* position
    - utter_role
* position{"role_type": "any"}
    - slot{"role_type": "any"}
    - action_check_positions
    - slot{"positions": ["machine learning engineer", "ML product success engineer"]}
    - utter_knowmore
* deny
    - utter_nothanks
    - utter_goodbye

## Generated Story -5383862420415068815
* thanks
    - utter_nothanks

## Generated Story -7705071050381947812
* status
    - utter_name
* name{"PERSON": "jibin mathew"}
    - slot{"PERSON": "jibin mathew"}
    - utter_check
    - action_check_status
    - slot{"status": "rejected"}
    - utter_knowmore
* deny
    - utter_nothanks
    - utter_goodbye

