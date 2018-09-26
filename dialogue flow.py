'''def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversaion."""
    import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    #for text in texts:
    text_input = dialogflow.types.TextInput(
        text=texts, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input)

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))


def explicit():
    from google.cloud import storage

    # Explicitly use service account credentials by specifying the private key
    # file.
    storage_client = storage.Client.from_service_account_json(
        'ADMINDROID-6aac4b557dcc.json')

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)

explicit()
project_id = "admindroid-7994f"
session_id = ""
texts = "kick out Swaroop"
language_code = "en"
'''

import os.path

import sys



try:

    import apiai

except ImportError:

    sys.path.append(

        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)

    )

    import apiai



CLIENT_ACCESS_TOKEN = '<client access token number'





def main():

    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)



    request = ai.text_request()



    request.lang = 'en'  # optional, default value equal 'en'



    request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"



    request.query = input("enter")



    response = request.getresponse()



    print (response.read())





if __name__ == '__main__':

    main()

