from huggingface_hub import login
from datasets import load_dataset, Dataset, concatenate_datasets
import json
from config import HF_TOKEN, DATASET_NAME

def init_huggingface():
    """Initialize Hugging Face authentication."""
    if HF_TOKEN is None:
        raise ValueError("Hugging Face token not found in environment variables.")
    login(token=HF_TOKEN)

def update_dataset(json_data):
    """Update the Hugging Face dataset with new data."""
    if json_data is None or json_data.startswith("The following fields are required"):
        return json_data or "No data to submit. Please fill in all required fields."

    try:
        data = json.loads(json_data)
    except json.JSONDecodeError:
        return "Invalid JSON data. Please ensure all required fields are filled correctly."
    
    try:
        dataset = load_dataset(DATASET_NAME, split="train")
    except:
        dataset = Dataset.from_dict({})

    new_data = create_flattened_data(data)
    new_dataset = Dataset.from_dict(new_data)
    
    if len(dataset) > 0:
        updated_dataset = concatenate_datasets([dataset, new_dataset])
    else:
        updated_dataset = new_dataset

    updated_dataset.push_to_hub(DATASET_NAME)
    return "Data submitted successfully and dataset updated!"

def create_flattened_data(data):
    """Create a flattened data structure for the dataset."""
    return {
        # Header
        "licensing": [data["header"]["licensing"]],
        "formatVersion": [data["header"]["formatVersion"]],
        "formatVersionSpecificationUri": [data["header"]["formatVersionSpecificationUri"]],
        "reportId": [data["header"]["reportId"]],
        "reportDatetime": [data["header"]["reportDatetime"]],
        "reportStatus": [data["header"]["reportStatus"]],
        "publisher_name": [data["header"]["publisher"]["name"]],
        "publisher_division": [data["header"]["publisher"]["division"]],
        "publisher_projectName": [data["header"]["publisher"]["projectName"]],
        "publisher_confidentialityLevel": [data["header"]["publisher"]["confidentialityLevel"]],
        "publisher_publicKey": [data["header"]["publisher"]["publicKey"]],
        
        # Task
        "taskType": [data["task"]["taskType"]],
        "taskFamily": [data["task"]["taskFamily"]],
        "taskStage": [data["task"]["taskStage"]],
        "algorithmName": [data["task"]["algorithms"][0]["algorithmName"]],
        "framework": [data["task"]["algorithms"][0]["framework"]],
        "frameworkVersion": [data["task"]["algorithms"][0]["frameworkVersion"]],
        "classPath": [data["task"]["algorithms"][0]["classPath"]],
        "tuning_method": [data["task"]["algorithms"][0]["hyperparameters"]["tuning_method"]],
        "hyperparameterName": [data["task"]["algorithms"][0]["hyperparameters"]["values"][0]["hyperparameterName"]],
        "hyperparameterValue": [data["task"]["algorithms"][0]["hyperparameters"]["values"][0]["hyperparameterValue"]],
        "quantization": [data["task"]["algorithms"][0]["quantization"]],
        "dataType": [data["task"]["dataset"][0]["dataType"]],
        "fileType": [data["task"]["dataset"][0]["fileType"]],
        "volume": [data["task"]["dataset"][0]["volume"]],
        "volumeUnit": [data["task"]["dataset"][0]["volumeUnit"]],
        "items": [data["task"]["dataset"][0]["items"]],
        "shape_item": [data["task"]["dataset"][0]["shape"][0]["item"]],
        "nbRequest": [data["task"]["dataset"][0]["inferenceProperties"][0]["nbRequest"]],
        "nbTokensInput": [data["task"]["dataset"][0]["inferenceProperties"][0]["parametersNLP"]["nbTokensInput"]],
        "nbWordsInput": [data["task"]["dataset"][0]["inferenceProperties"][0]["parametersNLP"]["nbWordsInput"]],
        "nbTokensOutput": [data["task"]["dataset"][0]["inferenceProperties"][0]["parametersNLP"]["nbTokensOutput"]],
        "nbWordsOutput": [data["task"]["dataset"][0]["inferenceProperties"][0]["parametersNLP"]["nbWordsOutput"]],
        "contextWindowSize": [data["task"]["dataset"][0]["inferenceProperties"][0]["parametersNLP"]["contextWindowSize"]],
        "cache": [data["task"]["dataset"][0]["inferenceProperties"][0]["parametersNLP"]["cache"]],
        "source": [data["task"]["dataset"][0]["source"]],
        "sourceUri": [data["task"]["dataset"][0]["sourceUri"]],
        "owner": [data["task"]["dataset"][0]["owner"]],
        "measuredAccuracy": [data["task"]["measuredAccuracy"]],
        "estimatedAccuracy": [data["task"]["estimatedAccuracy"]],
        
        # Measures
        "measurementMethod": [data["measures"][0]["measurementMethod"]],
        "manufacturer": [data["measures"][0]["manufacturer"]],
        "version": [data["measures"][0]["version"]],
        "cpuTrackingMode": [data["measures"][0]["cpuTrackingMode"]],
        "gpuTrackingMode": [data["measures"][0]["gpuTrackingMode"]],
        "averageUtilizationCpu": [data["measures"][0]["averageUtilizationCpu"]],
        "averageUtilizationGpu": [data["measures"][0]["averageUtilizationGpu"]],
        "serverSideInference": [data["measures"][0]["serverSideInference"]],
        "unit": [data["measures"][0]["unit"]],
        "powerCalibrationMeasurement": [data["measures"][0]["powerCalibrationMeasurement"]],
        "durationCalibrationMeasurement": [data["measures"][0]["durationCalibrationMeasurement"]],
        "powerConsumption": [data["measures"][0]["powerConsumption"]],
        "measurementDuration": [data["measures"][0]["measurementDuration"]],
        "measurementDateTime": [data["measures"][0]["measurementDateTime"]],
        
        # System
        "os": [data["system"]["os"]],
        "distribution": [data["system"]["distribution"]],
        "distributionVersion": [data["system"]["distributionVersion"]],
        
        # Software
        "language": [data["software"]["language"]],
        "version_software": [data["software"]["version"]],
        
        # Infrastructure
        "infraType": [data["infrastructure"]["infraType"]],
        "cloudProvider": [data["infrastructure"]["cloudProvider"]],
        "cloudInstance": [data["infrastructure"]["cloudInstance"]],
        "componentName": [data["infrastructure"]["components"][0]["componentName"]],
        "nbComponent": [data["infrastructure"]["components"][0]["nbComponent"]],
        "memorySize": [data["infrastructure"]["components"][0]["memorySize"]],
        "manufacturer_infra": [data["infrastructure"]["components"][0]["manufacturer"]],
        "family": [data["infrastructure"]["components"][0]["family"]],
        "series": [data["infrastructure"]["components"][0]["series"]],
        "share": [data["infrastructure"]["components"][0]["share"]],
        
        # Environment
        "country": [data["environment"]["country"]],
        "latitude": [data["environment"]["latitude"]],
        "longitude": [data["environment"]["longitude"]],
        "location": [data["environment"]["location"]],
        "powerSupplierType": [data["environment"]["powerSupplierType"]],
        "powerSource": [data["environment"]["powerSource"]],
        "powerSourceCarbonIntensity": [data["environment"]["powerSourceCarbonIntensity"]],
        
        # Quality
        "quality": [data["quality"]],
        
        # Hash
        "hashAlgorithm": [data["$hash"]["hashAlgorithm"]],
        "cryptographicAlgorithm": [data["$hash"]["cryptographicAlgorithm"]],
        "value": [data["$hash"]["value"]]
    }