class InputValidationError(Exception):
    """Custom exception for input validation error"""
    pass

def generate_feedback(user_input):

    if user_input['model_name'] != 'bert-base-uncased':
        raise InputValidationError("Check the model name. Ensure it's the standard BERT base model.")
    if user_input['tokenizer_name'] != 'BertTokenizer':
        raise InputValidationError("Verify the tokenizer name.")
    if user_input['text_email'] != 'sample_email':
        raise InputValidationError("You should tokenize the 'sample_email' text. Double-check the variable used.")
    if user_input['token_to_model'] != '**tokens':
        raise InputValidationError("Ensure you are passing the tokenized output to the model correctly.")
    if user_input['last_hidden_state'] != 'last_hidden_state':
        raise InputValidationError("Retrieve the 'last_hidden_state' from the model's output for the features.")


def test_learner_input():
    user_input = {
        'model_name':'bert-base-uncased',
        'tokenizer_name': 'BertTokenizer',
        'text_email': 'sample_email',
        'token_to_model': '**tokens',
        'last_hidden_state': 'last_hidden_state'

    }
    try:
        generate_feedback(user_input)
    except InputValidationError as err:
        assert False, f"Input Validation Error: {str(err)}"