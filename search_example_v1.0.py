import swagger_client
from swagger_client.models import *
from swagger_client.rest import ApiException
import sys

# Configuration
configuration = swagger_client.configuration.Configuration()
configuration.verify_ssl = False
configuration.host = "http://localhost:7761/v1.0"
api_config = swagger_client.ApiClient(configuration)

gsi_boards_apis = swagger_client.BoardsApi(api_config)
gsi_datasets_apis = swagger_client.DatasetsApi(api_config)
gsi_search_apis = swagger_client.SearchApi(api_config)

# Inputs
num_of_boards = 1
dataset_path = "/home/public/gsi-hermes-api/dataset_128k.npy"
queries_path = "/home/public/gsi-hermes-api/queries_20.npy"

# Example
dataset_id = '517d2548-8914-4428-b1d5-21257537e917' #'f30c520b-d4e9-4be1-a696-5f9a18896eeb' # Set to 'None' if you need to import the dataset
allocation_id = None
try:

    if not dataset_id:

        print("importing dataset", dataset_path)
        # Import Dataset
        response = gsi_datasets_apis.apis_import_dataset(body=ImportDatasetRequest(
            ds_file_path=dataset_path,
            ds_file_type="npy",
            train_ind=True))
        dataset_id = response.dataset_id

    print("using dataset_id=", dataset_id)

    # Allocate Board/s
    response = gsi_boards_apis.apis_allocate(body=AllocateRequest(
            num_of_boards=1,
            max_num_of_threads=5))
    allocation_id = response.allocation_id
    print("Got allocation_id=",allocation_id)

    # Load Dataset
    print("loading dataset", dataset_id)
    gsi_datasets_apis.apis_load_dataset(body=LoadDatasetRequest(allocation_id, dataset_id, topk=25))
    print("load done")

    # Search
    print("performing search")
    search_api_response = gsi_search_apis.apis_search(body=SearchRequest(allocation_id, dataset_id, queries_file_path=queries_path))
    indices = search_api_response.indices
    distance = search_api_response.distance
    metadata = search_api_response.metadata
    print("search done", len(indices), type(indices))

    # Unload Dataset
    print("unloading dataset")
    gsi_datasets_apis.apis_unload_dataset(body=UnloadDatasetRequest(allocation_id, dataset_id))
    print("done unload")

except ApiException as e:
    print(e.status)
    print(e.body)
    print(e.reason)
    raise e

finally:
    # Deallocate Board/s
    if allocation_id is not None:
        print("final deallocation", allocation_id)
        gsi_boards_apis.apis_deallocate(body=DeallocateRequest(allocation_id))





