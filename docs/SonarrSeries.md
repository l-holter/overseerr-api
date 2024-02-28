# SonarrSeries


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_options** | [**List[SonarrSeriesAddOptionsInner]**](SonarrSeriesAddOptionsInner.md) |  | [optional] 
**added** | **str** |  | [optional] 
**air_time** | **str** |  | [optional] 
**certification** | **str** |  | [optional] 
**clean_title** | **str** |  | [optional] 
**first_aired** | **str** |  | [optional] 
**genres** | **List[str]** |  | [optional] 
**id** | **float** |  | [optional] 
**images** | [**List[SonarrSeriesImagesInner]**](SonarrSeriesImagesInner.md) |  | [optional] 
**imdb_id** | **str** |  | [optional] 
**language_profile_id** | **float** |  | [optional] 
**last_info_sync** | **str** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**network** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**profile_id** | **float** |  | [optional] 
**quality_profile_id** | **float** |  | [optional] 
**ratings** | [**List[SonarrSeriesRatingsInner]**](SonarrSeriesRatingsInner.md) |  | [optional] 
**remote_poster** | **str** |  | [optional] 
**root_folder_path** | **str** |  | [optional] 
**runtime** | **float** |  | [optional] 
**season_count** | **float** |  | [optional] 
**season_folder** | **bool** |  | [optional] 
**seasons** | [**List[SonarrSeriesSeasonsInner]**](SonarrSeriesSeasonsInner.md) |  | [optional] 
**series_type** | **str** |  | [optional] 
**sort_title** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**title_slug** | **str** |  | [optional] 
**tv_maze_id** | **float** |  | [optional] 
**tv_rage_id** | **float** |  | [optional] 
**tvdb_id** | **float** |  | [optional] 
**use_scene_numbering** | **bool** |  | [optional] 
**year** | **float** |  | [optional] 

## Example

```python
from overseerr_api.models.sonarr_series import SonarrSeries

# TODO update the JSON string below
json = "{}"
# create an instance of SonarrSeries from a JSON string
sonarr_series_instance = SonarrSeries.from_json(json)
# print the JSON string representation of the object
print SonarrSeries.to_json()

# convert the object into a dict
sonarr_series_dict = sonarr_series_instance.to_dict()
# create an instance of SonarrSeries from a dict
sonarr_series_form_dict = sonarr_series.from_dict(sonarr_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


