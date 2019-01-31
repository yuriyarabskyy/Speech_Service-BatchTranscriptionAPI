# swagger-client
Speech Services API v2.0.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v2.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: subscription_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomSpeechSubscriptionsManagementApi(swagger_client.ApiClient(configuration))
move_to_subscription_definition = swagger_client.MoveToSubscriptionDefinition() # MoveToSubscriptionDefinition | The details of the subscription the entities are moved to.

try:
    # Initiates a task that moves all entities associated with the authenticated subscription to another one.
    api_instance.post_move_to_subscription(move_to_subscription_definition)
except ApiException as e:
    print("Exception when calling CustomSpeechSubscriptionsManagementApi->post_move_to_subscription: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://develop.cris.ai*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CustomSpeechSubscriptionsManagementApi* | [**post_move_to_subscription**](docs/CustomSpeechSubscriptionsManagementApi.md#post_move_to_subscription) | **POST** /api/common/v2.0/subscriptions | Initiates a task that moves all entities associated with the authenticated subscription to another one.
*CustomSpeechAccuracyTestsApi* | [**create_accuracy_test**](docs/CustomSpeechAccuracyTestsApi.md#create_accuracy_test) | **POST** /api/speechtotext/v2.0/accuracytests | Creates a new accuracy test.
*CustomSpeechAccuracyTestsApi* | [**delete_accuracy_test**](docs/CustomSpeechAccuracyTestsApi.md#delete_accuracy_test) | **DELETE** /api/speechtotext/v2.0/accuracytests/{id} | Deletes the accuracy test identified by the given ID.
*CustomSpeechAccuracyTestsApi* | [**get_accuracy_test**](docs/CustomSpeechAccuracyTestsApi.md#get_accuracy_test) | **GET** /api/speechtotext/v2.0/accuracytests/{id} | Gets the accuracy test identified by the given ID.
*CustomSpeechAccuracyTestsApi* | [**get_accuracy_tests**](docs/CustomSpeechAccuracyTestsApi.md#get_accuracy_tests) | **GET** /api/speechtotext/v2.0/accuracytests | Gets the list of accuracy tests for the authenticated subscription.
*CustomSpeechAccuracyTestsApi* | [**update_accuracy_test**](docs/CustomSpeechAccuracyTestsApi.md#update_accuracy_test) | **PATCH** /api/speechtotext/v2.0/accuracytests/{id} | Updates the mutable details of the test identified by its id.
*CustomSpeechDatasetsForModelAdaptationApi* | [**delete_dataset**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#delete_dataset) | **DELETE** /api/speechtotext/v2.0/datasets/{id} | Deletes the specified dataset.
*CustomSpeechDatasetsForModelAdaptationApi* | [**get_dataset**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#get_dataset) | **GET** /api/speechtotext/v2.0/datasets/{id} | Gets the dataset identified by the given ID.
*CustomSpeechDatasetsForModelAdaptationApi* | [**get_datasets**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#get_datasets) | **GET** /api/speechtotext/v2.0/datasets | Gets a list of datasets for the authenticated subscription.
*CustomSpeechDatasetsForModelAdaptationApi* | [**get_supported_locales_for_datasets**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#get_supported_locales_for_datasets) | **GET** /api/speechtotext/v2.0/datasets/locales | Gets a list of supported locales for data imports.
*CustomSpeechDatasetsForModelAdaptationApi* | [**update_dataset**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#update_dataset) | **PATCH** /api/speechtotext/v2.0/datasets/{id} | Updates the mutable details of the dataset identified by its ID.
*CustomSpeechDatasetsForModelAdaptationApi* | [**upload_dataset**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#upload_dataset) | **POST** /api/speechtotext/v2.0/datasets/upload | Uploads data and creates a new dataset.
*CustomSpeechEndpointsApi* | [**create_endpoint**](docs/CustomSpeechEndpointsApi.md#create_endpoint) | **POST** /api/speechtotext/v2.0/endpoints | Creates a new endpoint.
*CustomSpeechEndpointsApi* | [**create_endpoint_data_export**](docs/CustomSpeechEndpointsApi.md#create_endpoint_data_export) | **POST** /api/speechtotext/v2.0/endpoints/{endpointId}/data | Create a new endpoint data export task.
*CustomSpeechEndpointsApi* | [**delete_endpoint**](docs/CustomSpeechEndpointsApi.md#delete_endpoint) | **DELETE** /api/speechtotext/v2.0/endpoints/{id} | Deletes the endpoint identified by the given ID.
*CustomSpeechEndpointsApi* | [**delete_endpoint_data**](docs/CustomSpeechEndpointsApi.md#delete_endpoint_data) | **DELETE** /api/speechtotext/v2.0/endpoints/{endpointId}/data | Deletes the transcriptions and captured audio files associated with the endpoint identified by the given ID.  Note: Deletion will happen in the background and can take up to a day.
*CustomSpeechEndpointsApi* | [**delete_endpoint_data_export**](docs/CustomSpeechEndpointsApi.md#delete_endpoint_data_export) | **DELETE** /api/speechtotext/v2.0/endpoints/{endpointId}/data/{id} | Deletes the endpoint data export task identified by the given ID.
*CustomSpeechEndpointsApi* | [**get_endpoint**](docs/CustomSpeechEndpointsApi.md#get_endpoint) | **GET** /api/speechtotext/v2.0/endpoints/{id} | Gets the endpoint identified by the given ID.
*CustomSpeechEndpointsApi* | [**get_endpoint_data_export**](docs/CustomSpeechEndpointsApi.md#get_endpoint_data_export) | **GET** /api/speechtotext/v2.0/endpoints/{endpointId}/data/{id} | Gets the specified endpoint data export task for the authenticated user.
*CustomSpeechEndpointsApi* | [**get_endpoint_data_exports**](docs/CustomSpeechEndpointsApi.md#get_endpoint_data_exports) | **GET** /api/speechtotext/v2.0/endpoints/{endpointId}/data | Gets the list of endpoint data export tasks for the authenticated user.
*CustomSpeechEndpointsApi* | [**get_endpoints**](docs/CustomSpeechEndpointsApi.md#get_endpoints) | **GET** /api/speechtotext/v2.0/endpoints | Gets the list of endpoints for the authenticated subscription.
*CustomSpeechEndpointsApi* | [**get_supported_locales_for_endpoints**](docs/CustomSpeechEndpointsApi.md#get_supported_locales_for_endpoints) | **GET** /api/speechtotext/v2.0/endpoints/locales | Gets a list of supported locales for endpoint creations.
*CustomSpeechEndpointsApi* | [**update_endpoint**](docs/CustomSpeechEndpointsApi.md#update_endpoint) | **PATCH** /api/speechtotext/v2.0/endpoints/{id} | Updates the metadata of the endpoint identified by the given ID.
*CustomSpeechModelsApi* | [**create_model**](docs/CustomSpeechModelsApi.md#create_model) | **POST** /api/speechtotext/v2.0/models | Creates a new model.
*CustomSpeechModelsApi* | [**delete_model**](docs/CustomSpeechModelsApi.md#delete_model) | **DELETE** /api/speechtotext/v2.0/models/{id} | Deletes the model identified by the given ID.
*CustomSpeechModelsApi* | [**get_model**](docs/CustomSpeechModelsApi.md#get_model) | **GET** /api/speechtotext/v2.0/models/{id} | Gets the model identified by the given ID.
*CustomSpeechModelsApi* | [**get_models**](docs/CustomSpeechModelsApi.md#get_models) | **GET** /api/speechtotext/v2.0/models | Gets the list of models for the authenticated subscription.
*CustomSpeechModelsApi* | [**get_supported_locales_for_models**](docs/CustomSpeechModelsApi.md#get_supported_locales_for_models) | **GET** /api/speechtotext/v2.0/models/locales | Gets a list of supported locales for model adaptation.
*CustomSpeechModelsApi* | [**update_model**](docs/CustomSpeechModelsApi.md#update_model) | **PATCH** /api/speechtotext/v2.0/models/{id} | Updates the metadata of the model identified by the given ID.
*CustomSpeechTranscriptionsApi* | [**create_transcription**](docs/CustomSpeechTranscriptionsApi.md#create_transcription) | **POST** /api/speechtotext/v2.0/transcriptions | Creates a new transcription.
*CustomSpeechTranscriptionsApi* | [**delete_transcription**](docs/CustomSpeechTranscriptionsApi.md#delete_transcription) | **DELETE** /api/speechtotext/v2.0/transcriptions/{id} | Deletes the specified transcription task.
*CustomSpeechTranscriptionsApi* | [**get_supported_locales_for_transcriptions**](docs/CustomSpeechTranscriptionsApi.md#get_supported_locales_for_transcriptions) | **GET** /api/speechtotext/v2.0/transcriptions/locales | Gets a list of supported locales for offline transcriptions.
*CustomSpeechTranscriptionsApi* | [**get_transcription**](docs/CustomSpeechTranscriptionsApi.md#get_transcription) | **GET** /api/speechtotext/v2.0/transcriptions/{id} | Gets the transcription identified by the given ID.
*CustomSpeechTranscriptionsApi* | [**get_transcriptions**](docs/CustomSpeechTranscriptionsApi.md#get_transcriptions) | **GET** /api/speechtotext/v2.0/transcriptions | Gets a list of transcriptions for the authenticated subscription.
*CustomSpeechTranscriptionsApi* | [**update_transcription**](docs/CustomSpeechTranscriptionsApi.md#update_transcription) | **PATCH** /api/speechtotext/v2.0/transcriptions/{id} | Updates the mutable details of the transcription identified by its ID.
*LanguageGenerationEndpointsApi* | [**create_language_generation_endpoint**](docs/LanguageGenerationEndpointsApi.md#create_language_generation_endpoint) | **POST** /api/languagegeneration/v2.0/Endpoints | Creates a new language generation endpoint.
*LanguageGenerationEndpointsApi* | [**delete_language_generation_endpoint**](docs/LanguageGenerationEndpointsApi.md#delete_language_generation_endpoint) | **DELETE** /api/languagegeneration/v2.0/Endpoints/{id} | Deletes the language generation model endpoint with the given id.
*LanguageGenerationEndpointsApi* | [**get_language_generation_endpoint**](docs/LanguageGenerationEndpointsApi.md#get_language_generation_endpoint) | **GET** /api/languagegeneration/v2.0/Endpoints/{id} | Gets the specified deployed language generation endpoint.
*LanguageGenerationEndpointsApi* | [**get_language_generation_endpoints**](docs/LanguageGenerationEndpointsApi.md#get_language_generation_endpoints) | **GET** /api/languagegeneration/v2.0/Endpoints | Gets all language generation endpoint of a subscription.
*LanguageGenerationEndpointsApi* | [**get_supported_locales_for_language_generation_endpoints**](docs/LanguageGenerationEndpointsApi.md#get_supported_locales_for_language_generation_endpoints) | **GET** /api/languagegeneration/v2.0/Endpoints/locales | Gets a list of supported locales for language generation endpoint creation.
*LanguageGenerationEndpointsApi* | [**update_language_generation_endpoint**](docs/LanguageGenerationEndpointsApi.md#update_language_generation_endpoint) | **PATCH** /api/languagegeneration/v2.0/Endpoints/{id} | Updates the mutable details of the language generation endpoint identified by its id.
*LanguageGenerationModelsApi* | [**create_language_generation_model**](docs/LanguageGenerationModelsApi.md#create_language_generation_model) | **POST** /api/languagegeneration/v2.0/Models | Creates a new language generation model.
*LanguageGenerationModelsApi* | [**delete_language_generation_model**](docs/LanguageGenerationModelsApi.md#delete_language_generation_model) | **DELETE** /api/languagegeneration/v2.0/Models/{id} | Deletes the language generation model with the given id.
*LanguageGenerationModelsApi* | [**get_language_generation_model**](docs/LanguageGenerationModelsApi.md#get_language_generation_model) | **GET** /api/languagegeneration/v2.0/Models/{id} | Gets the specified language generation model.
*LanguageGenerationModelsApi* | [**get_language_generation_models**](docs/LanguageGenerationModelsApi.md#get_language_generation_models) | **GET** /api/languagegeneration/v2.0/Models | Gets all language generation model of a subscription.
*LanguageGenerationModelsApi* | [**get_supported_locales_for_language_generation_models**](docs/LanguageGenerationModelsApi.md#get_supported_locales_for_language_generation_models) | **GET** /api/languagegeneration/v2.0/Models/locales | Gets a list of supported locales for language generation model creation.
*LanguageGenerationModelsApi* | [**update_language_generation_model**](docs/LanguageGenerationModelsApi.md#update_language_generation_model) | **PATCH** /api/languagegeneration/v2.0/Models/{id} | Updates the mutable details of the language generation model identified by its id.
*ServiceHealthApi* | [**get_health_status**](docs/ServiceHealthApi.md#get_health_status) | **GET** /api/common/v2.0/healthstatus | The action returns the health of the different components of the serivce.
*VoiceDatasetsApi* | [**delete_voice_dataset**](docs/VoiceDatasetsApi.md#delete_voice_dataset) | **DELETE** /api/texttospeech/v2.0/datasets/{id} | Deletes the voice dataset with the given id.
*VoiceDatasetsApi* | [**get_supported_locales_for_voice_datasets**](docs/VoiceDatasetsApi.md#get_supported_locales_for_voice_datasets) | **GET** /api/texttospeech/v2.0/datasets/locales | Gets a list of supported locales for custom voice data imports.
*VoiceDatasetsApi* | [**get_voice_datasets**](docs/VoiceDatasetsApi.md#get_voice_datasets) | **GET** /api/texttospeech/v2.0/datasets | Gets all voice datasets of a user.
*VoiceDatasetsApi* | [**update_voice_dataset**](docs/VoiceDatasetsApi.md#update_voice_dataset) | **PATCH** /api/texttospeech/v2.0/datasets/{id} | Updates the mutable details of the voice dataset identified by its ID.
*VoiceDatasetsApi* | [**upload_voice_dataset**](docs/VoiceDatasetsApi.md#upload_voice_dataset) | **POST** /api/texttospeech/v2.0/datasets/upload | Uploads data and creates a new voice data object.
*VoiceEndpointsApi* | [**create_voice_deployment**](docs/VoiceEndpointsApi.md#create_voice_deployment) | **POST** /api/texttospeech/v2.0/endpoints | Creates a new voice endpoint object.
*VoiceEndpointsApi* | [**delete_deployment**](docs/VoiceEndpointsApi.md#delete_deployment) | **DELETE** /api/texttospeech/v2.0/endpoints/{id} | Delete the specified voice endpoint.
*VoiceEndpointsApi* | [**get_supported_locales_for_voice_endpoints**](docs/VoiceEndpointsApi.md#get_supported_locales_for_voice_endpoints) | **GET** /api/texttospeech/v2.0/endpoints/locales | Gets a list of supported locales for custom voice Endpoints.
*VoiceEndpointsApi* | [**get_voice_deployment**](docs/VoiceEndpointsApi.md#get_voice_deployment) | **GET** /api/texttospeech/v2.0/endpoints/{id} | Gets the details of a Custom Voice endpoint.
*VoiceEndpointsApi* | [**get_voice_deployments**](docs/VoiceEndpointsApi.md#get_voice_deployments) | **GET** /api/texttospeech/v2.0/endpoints | Gets a list of voice endpoint details.
*VoiceEndpointsApi* | [**update_voice_endpoint**](docs/VoiceEndpointsApi.md#update_voice_endpoint) | **PATCH** /api/texttospeech/v2.0/endpoints/{id} | Updates the name and description of the endpoint identified by the given ID.
*VoiceModelsApi* | [**create_voice_model**](docs/VoiceModelsApi.md#create_voice_model) | **POST** /api/texttospeech/v2.0/models | Creates a new voice model object.
*VoiceModelsApi* | [**delete_voice_model**](docs/VoiceModelsApi.md#delete_voice_model) | **DELETE** /api/texttospeech/v2.0/models/{id} | Deletes the voice model with the given id.
*VoiceModelsApi* | [**get_supported_locales_for_voice_models**](docs/VoiceModelsApi.md#get_supported_locales_for_voice_models) | **GET** /api/texttospeech/v2.0/models/locales | Gets a list of supported locales for custom voice Models.
*VoiceModelsApi* | [**get_voice_model**](docs/VoiceModelsApi.md#get_voice_model) | **GET** /api/texttospeech/v2.0/models/{id} | Gets specified voice model details.
*VoiceModelsApi* | [**get_voice_models**](docs/VoiceModelsApi.md#get_voice_models) | **GET** /api/texttospeech/v2.0/models | Gets a list of voice model details.
*VoiceModelsApi* | [**update_voice_model**](docs/VoiceModelsApi.md#update_voice_model) | **PATCH** /api/texttospeech/v2.0/models/{id} | Updates the metadata of the voice model identified by the given ID.
*VoiceTestsApi* | [**create_voice_test**](docs/VoiceTestsApi.md#create_voice_test) | **POST** /api/texttospeech/v2.0/tests | Creates a new voice test.
*VoiceTestsApi* | [**delete_voice_test**](docs/VoiceTestsApi.md#delete_voice_test) | **DELETE** /api/texttospeech/v2.0/tests/{id} | Deletes the specified voice test.
*VoiceTestsApi* | [**get_voice_test**](docs/VoiceTestsApi.md#get_voice_test) | **GET** /api/texttospeech/v2.0/tests/{id} | Gets detail of the specified voice test.


## Documentation For Models

 - [Component](docs/Component.md)
 - [Dataset](docs/Dataset.md)
 - [DatasetDefinition](docs/DatasetDefinition.md)
 - [DatasetIdentity](docs/DatasetIdentity.md)
 - [DatasetUpdate](docs/DatasetUpdate.md)
 - [Endpoint](docs/Endpoint.md)
 - [EndpointData](docs/EndpointData.md)
 - [EndpointDataDefinition](docs/EndpointDataDefinition.md)
 - [EndpointDefinition](docs/EndpointDefinition.md)
 - [EndpointUpdate](docs/EndpointUpdate.md)
 - [ErrorContent](docs/ErrorContent.md)
 - [ErrorDetail](docs/ErrorDetail.md)
 - [HealthStatusResponse](docs/HealthStatusResponse.md)
 - [IReadOnlyDictionary2](docs/IReadOnlyDictionary2.md)
 - [IReadOnlyDictionary21](docs/IReadOnlyDictionary21.md)
 - [InnerError](docs/InnerError.md)
 - [Model](docs/Model.md)
 - [ModelDefinition](docs/ModelDefinition.md)
 - [ModelIdentity](docs/ModelIdentity.md)
 - [ModelUpdate](docs/ModelUpdate.md)
 - [MoveToSubscriptionDefinition](docs/MoveToSubscriptionDefinition.md)
 - [SpeechEndpointDefinition](docs/SpeechEndpointDefinition.md)
 - [SpeechModelDefinition](docs/SpeechModelDefinition.md)
 - [Test](docs/Test.md)
 - [TestDefinition](docs/TestDefinition.md)
 - [TestUpdate](docs/TestUpdate.md)
 - [Transcription](docs/Transcription.md)
 - [TranscriptionDefinition](docs/TranscriptionDefinition.md)
 - [TranscriptionUpdate](docs/TranscriptionUpdate.md)
 - [VoiceTest](docs/VoiceTest.md)
 - [VoiceTestDefinition](docs/VoiceTestDefinition.md)
 - [WebHookConfigurationSecret](docs/WebHookConfigurationSecret.md)
 - [WebHookUpdate](docs/WebHookUpdate.md)


## Documentation For Authorization


## subscription_key

- **Type**: API key
- **API key parameter name**: Ocp-Apim-Subscription-Key
- **Location**: HTTP header


## Author

crservice@microsoft.com
