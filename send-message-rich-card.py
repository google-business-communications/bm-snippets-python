# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This code sends a rich card to the user with a fallback text.
# Read more: https://developers.google.com/business-communications/business-messages/guides/how-to/message/send?hl=en#rich-cards

# This code is based on the https://github.com/google-business-communications/python-businessmessages
# Python Business Messages client library.

# Edit the values below:
path_to_service_account_key = './service_account_key.json'
conversation_id = 'EDIT_HERE'

import json
import uuid

from businessmessages import businessmessages_v1_client as bm_client
from businessmessages.businessmessages_v1_messages import (
    BusinessMessagesCardContent, BusinessMessagesContentInfo,
    BusinessmessagesConversationsMessagesCreateRequest, BusinessMessagesMedia,
    BusinessMessagesMessage, BusinessMessagesRepresentative,
    BusinessMessagesRichCard, BusinessMessagesStandaloneCard,
    BusinessMessagesSuggestedReply, BusinessMessagesSuggestion)
from oauth2client.service_account import ServiceAccountCredentials

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    path_to_service_account_key,
    scopes=['https://www.googleapis.com/auth/businessmessages'])

client = bm_client.BusinessmessagesV1(credentials=credentials)

representativeTypeAsString = 'BOT'
if representativeTypeAsString == 'BOT':
    representativeType = BusinessMessagesRepresentative.RepresentativeTypeValueValuesEnum.BOT
else:
    representativeType = BusinessMessagesRepresentative.RepresentativeTypeValueValuesEnum.HUMAN

# Create a rich card message with two suggested replies and fallback text
message = BusinessMessagesMessage(
    messageId=str(uuid.uuid4().int),
    representative=BusinessMessagesRepresentative(
        representativeType=representativeType
    ),
    fallback='Hello, world!\nSent with Business Messages\n\nReply with \"Suggestion #1\" or \"Suggestion #2\"',
    richCard=BusinessMessagesRichCard(
        standaloneCard=BusinessMessagesStandaloneCard(
            cardContent=BusinessMessagesCardContent(
                title='Hello, world!',
                description='Sent with Business Messages.',
                suggestions=[
                  BusinessMessagesSuggestion(
                      reply=BusinessMessagesSuggestedReply(
                          text='Suggestion #1',
                          postbackData='suggestion_1')
                      ),
                  BusinessMessagesSuggestion(
                      reply=BusinessMessagesSuggestedReply(
                          text='Suggestion #2',
                          postbackData='suggestion_2')
                      )
                ],
                media=BusinessMessagesMedia(
                    height=BusinessMessagesMedia.HeightValueValuesEnum.TALL,
                    contentInfo=BusinessMessagesContentInfo(
                        altText='Google logo',
                        fileUrl='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
                        forceRefresh=False
                    ))
                ))))

# Create the message request
create_request = BusinessmessagesConversationsMessagesCreateRequest(
    businessMessagesMessage=message,
    parent='conversations/' + conversation_id)

# Send the message
bm_client.BusinessmessagesV1.ConversationsMessagesService(
    client=client).Create(request=create_request)
