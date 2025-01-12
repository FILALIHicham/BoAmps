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
    hyperparameterName, hyperparameterValue, quantization, dataType, fileType, volume, volumeUnit, items,
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
                        "values": [
                            {
                                "hyperparameterName": hyperparameterName,
                                "hyperparameterValue": hyperparameterValue
                            }
                        ]
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
                    "inferenceProperties": [
                        {
                            "nbRequest": nbRequest,
                            "parametersNLP": {
                                "nbTokensInput": nbTokensInput,
                                "nbWordsInput": nbWordsInput,
                                "nbTokensOutput": nbTokensOutput,
                                "nbWordsOutput": nbWordsOutput,
                                "contextWindowSize": contextWindowSize,
                                "cache": cache
                            }
                        }
                    ],
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
            "components": [
                {
                    "componentName": componentName,
                    "nbComponent": nbComponent,
                    "memorySize": memorySize,
                    "manufacturer": manufacturer_infra,
                    "family": family,
                    "series": series,
                    "share": share
                }
            ]
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
            "value": value_hash
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