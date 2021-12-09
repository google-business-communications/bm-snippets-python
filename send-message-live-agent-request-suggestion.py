# This code is based on the https://github.com/google-business-communications/python-businessmessages
# Python Business Messages client library.

# Edit the values below:
path_to_service_account_key = './service_account_key.json'
conversation_id = 'EDIT_HERE'

import json
import uuid

from businessmessages import businessmessages_v1_client as bm_client
from businessmessages.businessmessages_v1_messages import (
    BusinessmessagesConversationsMessagesCreateRequest,
    BusinessMessagesLiveAgentRequest, BusinessMessagesMessage,
    BusinessMessagesRepresentative, BusinessMessagesSuggestion)
from oauth2client.service_account import ServiceAccountCredentials

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    path_to_service_account_key,
    scopes=['https://www.googleapis.com/auth/businessmessages'])

client = bm_client.BusinessmessagesV1(credentials=credentials)

# Create a text message with a live agent request action
message = BusinessMessagesMessage(
    messageId=str(uuid.uuid4().int),
    representative=BusinessMessagesRepresentative( # Must be sent from a BOT representative
        representativeType=BusinessMessagesRepresentative.RepresentativeTypeValueValuesEnum.BOT
    ),
    text='Would you like to chat with a live agent?',
    fallback='Would you like to chat with a live agent?',
    suggestions=[
        BusinessMessagesSuggestion(
            liveAgentRequest=BusinessMessagesLiveAgentRequest()
        )
    ])

# Create the message request
create_request = BusinessmessagesConversationsMessagesCreateRequest(
    businessMessagesMessage=message,
    parent='conversations/' + conversation_id)

# Send the message
bm_client.BusinessmessagesV1.ConversationsMessagesService(
    client=client).Create(request=create_request)
