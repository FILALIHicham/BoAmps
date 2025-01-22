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
    # Handle hyperparameters
    hyperparameters = data.get("task", {}).get("algorithms", [{}])[0].get("hyperparameters", {}).get("values", [])

    # Process hyperparameters
    hyperparameter_names = []
    hyperparameter_values = []
    for hp in hyperparameters:
        if "name" in hp and "value" in hp:  # Match the keys used in JSON
            hyperparameter_names.append(hp["name"])
            hyperparameter_values.append(str(hp["value"]))

    hyperparameter_name_str = ", ".join(hyperparameter_names) if hyperparameter_names else None
    hyperparameter_value_str = ", ".join(hyperparameter_values) if hyperparameter_values else None

    # Handle inference properties
    inference_props = data.get("task", {}).get("dataset", [{}])[0].get("inferenceProperties", [])
    print("Extracted inference properties:", inference_props)

    # Process inference properties
    inference_data = []
    for props in inference_props:
        if props:  
            inference_data.append({
                "nbRequest": props.get("nbRequest"),
                "nbTokensInput": props.get("nbTokensInput"),
                "nbWordsInput": props.get("nbWordsInput"),
                "nbTokensOutput": props.get("nbTokensOutput"),
                "nbWordsOutput": props.get("nbWordsOutput"),
                "contextWindowSize": props.get("contextWindowSize"),
                "cache": props.get("cache")
            })

    nbRequest_str = ", ".join([str(p["nbRequest"]) for p in inference_data if p.get("nbRequest")]) if inference_data else None
    nbTokensInput_str = ", ".join([str(p["nbTokensInput"]) for p in inference_data if p.get("nbTokensInput")]) if inference_data else None
    nbWordsInput_str = ", ".join([str(p["nbWordsInput"]) for p in inference_data if p.get("nbWordsInput")]) if inference_data else None
    nbTokensOutput_str = ", ".join([str(p["nbTokensOutput"]) for p in inference_data if p.get("nbTokensOutput")]) if inference_data else None
    nbWordsOutput_str = ", ".join([str(p["nbWordsOutput"]) for p in inference_data if p.get("nbWordsOutput")]) if inference_data else None
    contextWindowSize_str = ", ".join([str(p["contextWindowSize"]) for p in inference_data if p.get("contextWindowSize")]) if inference_data else None
    cache_str = ", ".join([str(p["cache"]) for p in inference_data if p.get("cache")]) if inference_data else None
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
        "hyperparameterName": [hyperparameter_name_str],
        "hyperparameterValue": [hyperparameter_value_str],
        "quantization": [data["task"]["algorithms"][0]["quantization"]],
        "dataType": [data["task"]["dataset"][0]["dataType"]],
        "fileType": [data["task"]["dataset"][0]["fileType"]],
        "volume": [data["task"]["dataset"][0]["volume"]],
        "volumeUnit": [data["task"]["dataset"][0]["volumeUnit"]],
        "items": [data["task"]["dataset"][0]["items"]],
        "shape_item": [data["task"]["dataset"][0]["shape"][0]["item"]],
        "nbRequest": [nbRequest_str],
        "nbTokensInput": [nbTokensInput_str],
        "nbWordsInput": [nbWordsInput_str],
        "nbTokensOutput": [nbTokensOutput_str],
        "nbWordsOutput": [nbWordsOutput_str],
        "contextWindowSize": [contextWindowSize_str],
        "cache": [cache_str],
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