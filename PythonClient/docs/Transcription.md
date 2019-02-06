# Transcription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | [**list[Model]**](Model.md) | A list of models used for the transcription.  The list may contain an acoustic model, a language model or both.  IF only one model is given, the base model will be used for the other part | 
**id** | **str** | The identifier of this entity | 
**recordings_url** | **str** | The location where to download the input data from | 
**locale** | **str** | The locale of the contained data | [optional] 
**results_urls** | **dict(str, str)** | The results Urls for the transcription | [optional] 
**status_message** | **str** | The failure reason for the transcription | [optional] 
**created_date_time** | **datetime** | The time-stamp when the object was created | 
**last_action_date_time** | **datetime** | The time-stamp when the current status was entered | 
**status** | **str** | The status of the object | 
**name** | **str** | The name of the object | 
**description** | **str** | The description of the object | [optional] 
**properties** | **dict(str, str)** | The custom properties of this entity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


