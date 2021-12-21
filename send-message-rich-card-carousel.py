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

"""This code sends to the user a carousel with rich cards and a fallback text.

Read more: https://developers.google.com/business-communications/business-messages/guides/how-to/message/send?hl=en#rich-card-carousels

This code is based on the https://github.com/google-business-communications/python-businessmessages
Python Business Messages client library.
"""

import uuid

from businessmessages import businessmessages_v1_client as bm_client
from businessmessages.businessmessages_v1_messages import BusinessMessagesCardContent
from businessmessages.businessmessages_v1_messages import BusinessMessagesCarouselCard
from businessmessages.businessmessages_v1_messages import BusinessMessagesContentInfo
from businessmessages.businessmessages_v1_messages import BusinessmessagesConversationsMessagesCreateRequest
from businessmessages.businessmessages_v1_messages import BusinessMessagesMedia
from businessmessages.businessmessages_v1_messages import BusinessMessagesMessage
from businessmessages.businessmessages_v1_messages import BusinessMessagesRepresentative
from businessmessages.businessmessages_v1_messages import BusinessMessagesRichCard
from businessmessages.businessmessages_v1_messages import BusinessMessagesSuggestedReply
from businessmessages.businessmessages_v1_messages import BusinessMessagesSuggestion
from oauth2client.service_account import ServiceAccountCredentials

# Edit the values below:
path_to_service_account_key = './service_account_key.json'
conversation_id = 'EDIT_HERE'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    path_to_service_account_key,
    scopes=['https://www.googleapis.com/auth/businessmessages'])

client = bm_client.BusinessmessagesV1(credentials=credentials)

representative_type_as_string = 'BOT'
if representative_type_as_string == 'BOT':
  representative_type = BusinessMessagesRepresentative.RepresentativeTypeValueValuesEnum.BOT
else:
  representative_type = BusinessMessagesRepresentative.RepresentativeTypeValueValuesEnum.HUMAN

# Create a carousel message with two cards and a suggested reply for each card
# and fallback text
message = BusinessMessagesMessage(
    messageId=str(uuid.uuid4().int),
    representative=BusinessMessagesRepresentative(
        representativeType=representative_type
    ),
    fallback='Card #1\nThe description for card #1\n\nCard #2\nThe description for card #2\n\nReply with \"Card #1\" or \"Card #2\"',
    richCard=BusinessMessagesRichCard(
        carouselCard=BusinessMessagesCarouselCard(
            cardWidth=BusinessMessagesCarouselCard.CardWidthValueValuesEnum.MEDIUM,
            cardContents=[
                BusinessMessagesCardContent(
                    title='Card #1',
                    description='The description for card #1',
                    suggestions=[
                        BusinessMessagesSuggestion(
                            reply=BusinessMessagesSuggestedReply(
                                text='Card #1',
                                postbackData='card_1')
                            )
                    ],
                    media=BusinessMessagesMedia(
                        height=BusinessMessagesMedia.HeightValueValuesEnum.MEDIUM,
                        contentInfo=BusinessMessagesContentInfo(
                            fileUrl='https://storage.googleapis.com/kitchen-sink-sample-images/cute-dog.jpg',
                            forceRefresh=False))),
                BusinessMessagesCardContent(
                    title='Card #2',
                    description='The description for card #2',
                    suggestions=[
                        BusinessMessagesSuggestion(
                            reply=BusinessMessagesSuggestedReply(
                                text='Card #2',
                                postbackData='card_2')
                            )
                    ],
                    media=BusinessMessagesMedia(
                        height=BusinessMessagesMedia.HeightValueValuesEnum.MEDIUM,
                        contentInfo=BusinessMessagesContentInfo(
                            fileUrl='https://storage.googleapis.com/kitchen-sink-sample-images/elephant.jpg',
                            forceRefresh=False)))
            ])))

# Create the message request
create_request = BusinessmessagesConversationsMessagesCreateRequest(
    businessMessagesMessage=message,
    parent='conversations/' + conversation_id)

# Send the message
bm_client.BusinessmessagesV1.ConversationsMessagesService(
    client=client).Create(request=create_request)
