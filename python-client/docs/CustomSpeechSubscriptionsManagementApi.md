# cris_client.CustomSpeechSubscriptionsManagementApi

All URIs are relative to *https://develop.cris.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_move_to_subscription**](CustomSpeechSubscriptionsManagementApi.md#post_move_to_subscription) | **POST** /api/common/v2.0/subscriptions | Initiates a task that moves all entities associated with the authenticated subscription to another one.


# **post_move_to_subscription**
> post_move_to_subscription(move_to_subscription_definition)

Initiates a task that moves all entities associated with the authenticated subscription to another one.

### Example
```python
from __future__ import print_function
import time
import cris_client
from cris_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: subscription_key
configuration = cris_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'

# create an instance of the API class
api_instance = cris_client.CustomSpeechSubscriptionsManagementApi(cris_client.ApiClient(configuration))
move_to_subscription_definition = cris_client.MoveToSubscriptionDefinition() # MoveToSubscriptionDefinition | The details of the subscription the entities are moved to.

try:
    # Initiates a task that moves all entities associated with the authenticated subscription to another one.
    api_instance.post_move_to_subscription(move_to_subscription_definition)
except ApiException as e:
    print("Exception when calling CustomSpeechSubscriptionsManagementApi->post_move_to_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_to_subscription_definition** | [**MoveToSubscriptionDefinition**](MoveToSubscriptionDefinition.md)| The details of the subscription the entities are moved to. | 

### Return type

void (empty response body)

### Authorization

[subscription_key](../README.md#subscription_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

