import gradio as gr
from config import (
    REPORT_STATUS_OPTIONS, CONFIDENTIALITY_LEVELS, DATA_TYPES,
    ACCURACY_LEVELS, MEASUREMENT_UNITS, INFRA_TYPES,
    POWER_SUPPLIER_TYPES, POWER_SOURCES, QUALITY_LEVELS,
    HASH_ALGORITHMS, CRYPTO_ALGORITHMS, CACHE_OPTIONS
)

def create_header_tab():
    """Create the header tab components."""
    with gr.Tab("Header"):
        licensing = gr.Textbox(label="Licensing", info="(the type of licensing applicable for the sharing of the report)")
        formatVersion = gr.Textbox(label="Format Version", info="Required field<br>(the version of the specification of this set of schemas defining the report's fields)")
        formatVersionSpecificationUri = gr.Textbox(label="Format Version Specification URI", info="(the URI of the present specification of this set of schemas)")
        reportId = gr.Textbox(label="Report ID", info="Required field<br>(the unique identifier of this report, preferably as a uuid4 string)")
        reportDatetime = gr.Textbox(label="Report Datetime", info="(the publishing date of this report in format YYYY-MM-DD HH:MM:SS)")
        reportStatus = gr.Dropdown(value=None,
            label="Report Status",
            choices=REPORT_STATUS_OPTIONS,
            info="Required field<br>(the status of this report)"
        )
        
        with gr.Accordion("Publisher"):
            publisher_name = gr.Textbox(label="Name", info="(name of the organization)")
            publisher_division = gr.Textbox(label="Division", info="(name of the publishing department within the organization)")
            publisher_projectName = gr.Textbox(label="Project Name", info="(name of the publishing project within the organization)")
            publisher_confidentialityLevel = gr.Dropdown(value=None,
                label="Confidentiality Level",
                choices=CONFIDENTIALITY_LEVELS,
                info="Required field<br>(the confidentiality of the report)"
            )
            publisher_publicKey = gr.Textbox(label="Public Key", info="(the cryptographic public key to check the identity of the publishing organization)")
        
        return [
            licensing, formatVersion, formatVersionSpecificationUri, reportId,
            reportDatetime, reportStatus, publisher_name, publisher_division,
            publisher_projectName, publisher_confidentialityLevel, publisher_publicKey
        ]

def create_task_tab():
    """Create the task tab components."""
    with gr.Tab("Task"):
        taskType = gr.Textbox(label="Task Type", info="Required field<br>(type of the computing task of machine learning, example : datacreation, preprocessing, supervisedLearning, unsupervisedLearning, semiSupervisedLearning ...)")
        taskFamily = gr.Textbox(label="Task Family", info="Required field<br>(the family of task performed, example : classification, regression, chatbot, summarization, keyword extraction, image recognition...)")
        taskStage = gr.Textbox(label="Task Stage", info="Required field<br>(stage of the task, example: training, finetuning, reinforcement, inference, rag...)")
        
        with gr.Accordion("Algorithms"):
            algorithmName = gr.Textbox(label="Algorithm Name", info="Required field<br>(the case-sensitive common name of the algorithm, example: randomForest, svm, xgboost...)")
            framework = gr.Textbox(label="Framework", info="(the common name of the software framework implementing the algorithm)")
            frameworkVersion = gr.Textbox(label="Framework Version", info="(the version of the software framework)")
            classPath = gr.Textbox(label="Class Path", info="(the full class path of the algorithm within the framework)")
            tuning_method = gr.Textbox(label="Tuning Method", info="(the method of hyperparameters tuning used (if any), example: gridSearch, randomizedSearch...)")
            
            with gr.Accordion("Hyperparameters"):
                with gr.Row():
                    hyperparameterName = gr.Textbox(label="Hyperparameter Name", info="(the name of the hyperparameter, example: c, kernel, gamma, class_weight...)")
                    hyperparameterValue = gr.Textbox(label="Hyperparameter Value", info="(the value of the hyperparameter, example: rbf, 1e-4, 10, linear...)")
            
            quantization = gr.Textbox(label="Quantization", info="(the data weights (in bits) obtained thanks to the quantization, example: 2, 8, 16...)")
        
        with gr.Accordion("Dataset"):
            dataType = gr.Dropdown(value=None,
                label="Data Type",
                choices=DATA_TYPES,
                info="Required field<br>(the nature of the data)"
            )
            fileType = gr.Textbox(label="File Type", info="(the file type of the dataset)")
            volume = gr.Textbox(label="Volume", info="Required field<br>(the size of the dataset)")
            volumeUnit = gr.Textbox(label="Volume Unit", info="Required field<br>(the unit of the size)")
            items = gr.Textbox(label="Items", info="(the number of items in the dataset)")
            shape_item = gr.Textbox(label="Shape Item", info="(the shape of each dataset item)")
            
            with gr.Accordion("Inference Properties"):
                nbRequest = gr.Textbox(label="Number of Requests", info="Required field<br>(the number of requests the measure corresponds to)")
                nbTokensInput = gr.Textbox(label="Number of Tokens Input", info="(the number of tokens in the input)")
                nbWordsInput = gr.Textbox(label="Number of Words Input", info="(the number of words in the input)")
                nbTokensOutput = gr.Textbox(label="Number of Tokens Output", info="(the number of tokens in the output)")
                nbWordsOutput = gr.Textbox(label="Number of Words Output", info="(the number of words in the output)")
                contextWindowSize = gr.Textbox(label="Context Window Size", info="(the number of tokens kept in memory)")
                cache = gr.Dropdown(value=None,
                    label="Cache",
                    choices=CACHE_OPTIONS,
                    info="(the presence of a cache function)"
                )
            
            source = gr.Textbox(label="Source", info="(the kind of source of the dataset)")
            sourceUri = gr.Textbox(label="Source URI", info="(the URI of the dataset)")
            owner = gr.Textbox(label="Owner", info="(the owner of the dataset)")

        with gr.Row():
            measuredAccuracy = gr.Textbox(label="Measured Accuracy", info="(the measured accuracy of your model (between 0 and 1))")
            estimatedAccuracy = gr.Dropdown(value=None,
                label="Estimated Accuracy",
                choices=ACCURACY_LEVELS,
                info="(estimated accuracy assessment)"
            )
        
        return [
            taskType, taskFamily, taskStage, algorithmName, framework,
            frameworkVersion, classPath, tuning_method, hyperparameterName,
            hyperparameterValue, quantization, dataType, fileType, volume,
            volumeUnit, items, shape_item, nbRequest, nbTokensInput,
            nbWordsInput, nbTokensOutput, nbWordsOutput, contextWindowSize,
            cache, source, sourceUri, owner, measuredAccuracy, estimatedAccuracy
        ]

def create_measures_tab():
    """Create the measures tab components."""
    with gr.Tab("Measures"):
        measurementMethod = gr.Textbox(label="Measurement Method", info="Required field<br>(the method used to perform the energy or FLOPS measure)")
        manufacturer = gr.Textbox(label="Manufacturer", info="(the builder of the measuring tool)")
        version = gr.Textbox(label="Version", info="(the version of the measuring tool)")
        cpuTrackingMode = gr.Textbox(label="CPU Tracking Mode", info="(the method used to track CPU consumption)")
        gpuTrackingMode = gr.Textbox(label="GPU Tracking Mode", info="(the method used to track GPU consumption)")
        averageUtilizationCpu = gr.Textbox(label="Average Utilization CPU", info="(the average percentage of CPU use)")
        averageUtilizationGpu = gr.Textbox(label="Average Utilization GPU", info="(the average percentage of GPU use)")
        serverSideInference = gr.Textbox(label="Server Side Inference", info="(inference server consumption estimation)")
        unit = gr.Dropdown(value=None,
            label="Unit",
            choices=MEASUREMENT_UNITS,
            info="Required field<br>(the unit of power consumption measure)"
        )
        powerCalibrationMeasurement = gr.Textbox(label="Power Calibration Measurement", info="(power consumed during calibration)")
        durationCalibrationMeasurement = gr.Textbox(label="Duration Calibration Measurement", info="(duration of calibration in seconds)")
        powerConsumption = gr.Textbox(label="Power Consumption", info="Required field<br>(the power consumption measure)")
        measurementDuration = gr.Textbox(label="Measurement Duration", info="(the duration of measurement in seconds)")
        measurementDateTime = gr.Textbox(label="Measurement DateTime", info="(when measurement began)")
        
        return [
            measurementMethod, manufacturer, version, cpuTrackingMode,
            gpuTrackingMode, averageUtilizationCpu, averageUtilizationGpu,
            serverSideInference, unit, powerCalibrationMeasurement,
            durationCalibrationMeasurement, powerConsumption,
            measurementDuration, measurementDateTime
        ]

def create_system_tab():
    """Create the system tab components."""
    with gr.Tab("System"):
        os = gr.Textbox(label="OS", info="Required field<br>(name of the operating system)")
        distribution = gr.Textbox(label="Distribution", info="(distribution of the operating system)")
        distributionVersion = gr.Textbox(label="Distribution Version", info="(distribution version)")
        
        return [os, distribution, distributionVersion]

def create_software_tab():
    """Create the software tab components."""
    with gr.Tab("Software"):
        language = gr.Textbox(label="Language", info="Required field<br>(programming language information)")
        version_software = gr.Textbox(label="Version", info="(version of the programming language)")
        
        return [language, version_software]

def create_infrastructure_tab():
    """Create the infrastructure tab components."""
    with gr.Tab("Infrastructure"):
        infraType = gr.Dropdown(value=None,
            label="Infrastructure Type",
            choices=INFRA_TYPES,
            info="Required field<br>(the type of infrastructure used)"
        )
        cloudProvider = gr.Textbox(label="Cloud Provider", info="(name of your cloud provider)")
        cloudInstance = gr.Textbox(label="Cloud Instance", info="(name of your cloud instance)")
        componentName = gr.Textbox(label="Component Name", info="Required field<br>(type of subsystem part)")
        nbComponent = gr.Textbox(label="Number of Components", info="Required field<br>(number of items of this component)")
        memorySize = gr.Textbox(label="Memory Size", info="(size of memory in Gbytes)")
        manufacturer_infra = gr.Textbox(label="Manufacturer", info="(name of the manufacturer)")
        family = gr.Textbox(label="Family", info="(family of this component)")
        series = gr.Textbox(label="Series", info="(series of this component)")
        share = gr.Textbox(label="Share", info="(percentage of equipment used)")
        
        return [
            infraType, cloudProvider, cloudInstance, componentName,
            nbComponent, memorySize, manufacturer_infra, family,
            series, share
        ]

def create_environment_tab():
    """Create the environment tab components."""
    with gr.Tab("Environment"):
        country = gr.Textbox(label="Country", info="Required field")
        latitude = gr.Textbox(label="Latitude")
        longitude = gr.Textbox(label="Longitude")
        location = gr.Textbox(label="Location")
        powerSupplierType = gr.Dropdown(value=None,
            label="Power Supplier Type",
            choices=POWER_SUPPLIER_TYPES,
            info="(the type of power supplier)"
        )
        powerSource = gr.Dropdown(value=None,
            label="Power Source",
            choices=POWER_SOURCES,
            info="(the source of power)"
        )
        powerSourceCarbonIntensity = gr.Textbox(label="Power Source Carbon Intensity")
        
        return [
            country, latitude, longitude, location,
            powerSupplierType, powerSource, powerSourceCarbonIntensity
        ]

def create_quality_tab():
    """Create the quality tab components."""
    with gr.Tab("Quality"):
        quality = gr.Dropdown(value=None,
            label="Quality",
            choices=QUALITY_LEVELS,
            info="(the quality of the information provided)"
        )
        
        return [quality]

def create_hash_tab():
    """Create the hash tab components."""
    with gr.Tab("Hash"):
        hashAlgorithm = gr.Dropdown(value=None,
            label="Hash Algorithm",
            choices=HASH_ALGORITHMS,
            info="Required field<br>(the hash function to apply)"
        )
        cryptographicAlgorithm = gr.Dropdown(value=None,
            label="Cryptographic Algorithm",
            choices=CRYPTO_ALGORITHMS,
            info="Required field<br>(the public key function to apply)"
        )
        value_hash = gr.Textbox(label="Value", info="Required field<br>(encrypted value of the hash)")
        
        return [hashAlgorithm, cryptographicAlgorithm, value_hash]