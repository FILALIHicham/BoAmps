import json
import tempfile
from datetime import datetime
from utils.validation import validate_obligatory_fields

def generate_json(
    # Header
    licensing, formatVersion, formatVersionSpecificationUri, reportId, reportDatetime, reportStatus,
    publisher_name, publisher_division, publisher_projectName, publisher_confidentialityLevel, publisher_publicKey,
    # Task
    taskType, taskFamily, taskStage, algorithmName, framework, frameworkVersion, classPath, tuning_method,
    hyperparameter_names, hyperparameter_values, quantization, dataType, fileType, volume, volumeUnit, items,
    shape_item, nbRequest, nbTokensInput, nbWordsInput, nbTokensOutput, nbWordsOutput, contextWindowSize, cache,
    source, sourceUri, owner, measuredAccuracy, estimatedAccuracy,
    # Measures
    measurementMethod, manufacturer, version, cpuTrackingMode, gpuTrackingMode, averageUtilizationCpu,
    averageUtilizationGpu, serverSideInference, unit, powerCalibrationMeasurement, durationCalibrationMeasurement,
    powerConsumption, measurementDuration, measurementDateTime,
    # System
    os, distribution, distributionVersion,
    # Software
    language, version_software,
    # Infrastructure
    infraType, cloudProvider, cloudInstance, componentName, nbComponent, memorySize, manufacturer_infra, family, series, share,
    # Environment
    country, latitude, longitude, location, powerSupplierType, powerSource, powerSourceCarbonIntensity,
    # Quality
    quality,
    # Hash
    hashAlgorithm, cryptographicAlgorithm, value_hash
):
    """Generate JSON data from form inputs."""
    # Process hyperparameters
    hyperparameters = []
    max_length = max(len(hyperparameter_names), len(hyperparameter_values))
    for i in range(max_length):
        hyperparameters.append({
            "name": hyperparameter_names[i] if i < len(hyperparameter_names) and hyperparameter_names[i] else "",
            "value": hyperparameter_values[i] if i < len(hyperparameter_values) and hyperparameter_values[i] else ""
        })
        
    # Process inference properties
    inference_props_list = []
    max_length = max(len(nbRequest), len(nbTokensInput), len(nbWordsInput), len(nbTokensOutput), len(nbWordsOutput), len(contextWindowSize), len(cache))
    for i in range(max_length):
        inference_props_list.append({
            "nbRequest": nbRequest[i] if i < len(nbRequest) and nbRequest[i] else "",
            "nbTokensInput": nbTokensInput[i] if i < len(nbTokensInput) and nbTokensInput[i] else "",
            "nbWordsInput": nbWordsInput[i] if i < len(nbWordsInput) and nbWordsInput[i] else "",
            "nbTokensOutput": nbTokensOutput[i] if i < len(nbTokensOutput) and nbTokensOutput[i] else "",
            "nbWordsOutput": nbWordsOutput[i] if i < len(nbWordsOutput) and nbWordsOutput[i] else "",
            "contextWindowSize": contextWindowSize[i] if i < len(contextWindowSize) and contextWindowSize[i] else "",
            "cache": cache[i] if i < len(cache) and cache[i] else ""
        })

    # Process components
    components_list = []
    max_length = max(len(componentName), len(nbComponent), len(memorySize), len(manufacturer_infra), len(family), len(series), len(share))
    for i in range(max_length):
        components_list.append({
            "componentName": componentName[i] if i < len(componentName) and componentName[i] else "",
            "nbComponent": nbComponent[i] if i < len(nbComponent) and nbComponent[i] else "",
            "memorySize": memorySize[i] if i < len(memorySize) and memorySize[i] else "",
            "manufacturer": manufacturer_infra[i] if i < len(manufacturer_infra) and manufacturer_infra[i] else "",
            "family": family[i] if i < len(family) and family[i] else "",
            "series": series[i] if i < len(series) and series[i] else "",
            "share": share[i] if i < len(share) and share[i] else ""
        })
    
    data = {
        "header": {
            "licensing": licensing,
            "formatVersion": formatVersion,
            "formatVersionSpecificationUri": formatVersionSpecificationUri,
            "reportId": reportId,
            "reportDatetime": reportDatetime or datetime.now().isoformat(),
            "reportStatus": reportStatus,
            "publisher": {
                "name": publisher_name,
                "division": publisher_division,
                "projectName": publisher_projectName,
                "confidentialityLevel": publisher_confidentialityLevel,
                "publicKey": publisher_publicKey
            }
        },
        "task": {
            "taskType": taskType,
            "taskFamily": taskFamily,
            "taskStage": taskStage,
            "algorithms": [
                {
                    "algorithmName": algorithmName,
                    "framework": framework,
                    "frameworkVersion": frameworkVersion,
                    "classPath": classPath,
                    "hyperparameters": {
                        "tuning_method": tuning_method,
                        "values": hyperparameters,
                    },
                    "quantization": quantization
                }
            ],
            "dataset": [
                {
                    "dataType": dataType,
                    "fileType": fileType,
                    "volume": volume,
                    "volumeUnit": volumeUnit,
                    "items": items,
                    "shape": [
                        {
                            "item": shape_item
                        }
                    ],
                    "inferenceProperties": inference_props_list,
                    "source": source,
                    "sourceUri": sourceUri,
                    "owner": owner
                }
            ],
            "measuredAccuracy": measuredAccuracy,
            "estimatedAccuracy": estimatedAccuracy
        },
        "measures": [
            {
                "measurementMethod": measurementMethod,
                "manufacturer": manufacturer,
                "version": version,
                "cpuTrackingMode": cpuTrackingMode,
                "gpuTrackingMode": gpuTrackingMode,
                "averageUtilizationCpu": averageUtilizationCpu,
                "averageUtilizationGpu": averageUtilizationGpu,
                "serverSideInference": serverSideInference,
                "unit": unit,
                "powerCalibrationMeasurement": powerCalibrationMeasurement,
                "durationCalibrationMeasurement": durationCalibrationMeasurement,
                "powerConsumption": powerConsumption,
                "measurementDuration": measurementDuration,
                "measurementDateTime": measurementDateTime
            }
        ],
        "system": {
            "os": os,
            "distribution": distribution,
            "distributionVersion": distributionVersion
        },
        "software": {
            "language": language,
            "version": version_software
        },
        "infrastructure": {
            "infraType": infraType,
            "cloudProvider": cloudProvider,
            "cloudInstance": cloudInstance,
            "components": components_list
        },
        "environment": {
            "country": country,
            "latitude": latitude,
            "longitude": longitude,
            "location": location,
            "powerSupplierType": powerSupplierType,
            "powerSource": powerSource,
            "powerSourceCarbonIntensity": powerSourceCarbonIntensity
        },
        "quality": quality,
        "$hash": {
            "hashAlgorithm": hashAlgorithm,
            "cryptographicAlgorithm": cryptographicAlgorithm,
            "ecryptedValue": value_hash
        }
    }

    # Validate obligatory fields
    is_valid, message = validate_obligatory_fields(data)
    if not is_valid:
        return message, None, ""
    
    # Create the JSON string
    json_str = json.dumps(data, indent=4)

    # Create and save the JSON file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        json.dump(data, f, indent=4)
        return message, f.name, json_str