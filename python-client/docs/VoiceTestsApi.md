# cris_client.VoiceTestsApi

All URIs are relative to *https://develop.cris.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_voice_test**](VoiceTestsApi.md#create_voice_test) | **POST** /api/texttospeech/v2.0/tests | Creates a new voice test.
[**delete_voice_test**](VoiceTestsApi.md#delete_voice_test) | **DELETE** /api/texttospeech/v2.0/tests/{id} | Deletes the specified voice test.
[**get_voice_test**](VoiceTestsApi.md#get_voice_test) | **GET** /api/texttospeech/v2.0/tests/{id} | Gets detail of the specified voice test.


# **create_voice_test**
> create_voice_test(voice_test_definition)

Creates a new voice test.

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
api_instance = cris_client.VoiceTestsApi(cris_client.ApiClient(configuration))
voice_test_definition = cris_client.VoiceTestDefinition() # VoiceTestDefinition | 

try:
    # Creates a new voice test.
    api_instance.create_voice_test(voice_test_definition)
except ApiException as e:
    print("Exception when calling VoiceTestsApi->create_voice_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voice_test_definition** | [**VoiceTestDefinition**](VoiceTestDefinition.md)|  | 

### Return type

void (empty response body)

### Authorization

[subscription_key](../README.md#subscription_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_voice_test**
> delete_voice_test(id)

Deletes the specified voice test.

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
api_instance = cris_client.VoiceTestsApi(cris_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the voice test.

try:
    # Deletes the specified voice test.
    api_instance.delete_voice_test(id)
except ApiException as e:
    print("Exception when calling VoiceTestsApi->delete_voice_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the voice test. | 

### Return type

void (empty response body)

### Authorization

[subscription_key](../README.md#subscription_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voice_test**
> VoiceTest get_voice_test(id)

Gets detail of the specified voice test.

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
api_instance = cris_client.VoiceTestsApi(cris_client.ApiClient(configuration))
id = 'id_example' # str | The identifier of the voice test.

try:
    # Gets detail of the specified voice test.
    api_response = api_instance.get_voice_test(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceTestsApi->get_voice_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the voice test. | 

### Return type

[**VoiceTest**](VoiceTest.md)

### Authorization

[subscription_key](../README.md#subscription_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

