# Job


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**interval** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**next_execution_time** | **str** |  | [optional] 
**running** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from overseerr_api.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print Job.to_json()

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_form_dict = job.from_dict(job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


