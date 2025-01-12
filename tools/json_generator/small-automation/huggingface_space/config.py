import os

# Hugging Face Configuration
HF_TOKEN = os.environ.get("HF_TOKEN")
DATASET_NAME = "FILALIHicham/EcoMindAI-Data"

# Form Field Configurations
OBLIGATORY_FIELDS = [
    "formatVersion", "reportId", "reportStatus", "confidentialityLevel",
    "taskType", "taskFamily", "taskStage", "algorithmName", "dataType",
    "volume", "volumeUnit", "nbRequest", "measurementMethod", "unit",
    "powerConsumption", "os", "language", "infraType", "componentName",
    "nbComponent", "country", "hashAlgorithm", "cryptographicAlgorithm", "value"
]

# Dropdown Options
REPORT_STATUS_OPTIONS = ["draft", "final", "corrective", "$other"]
CONFIDENTIALITY_LEVELS = ["public", "internal", "confidential", "secret"]
DATA_TYPES = ["tabular", "audio", "boolean", "image", "video", "object", "text", "$other"]
ACCURACY_LEVELS = ["veryPoor", "poor", "average", "good", "veryGood"]
MEASUREMENT_UNITS = ["Wh", "kWh", "MWh", "GWh", "kJoule", "MJoule", "GJoule", "TJoule", "PJoule", 
                    "BTU", "kiloFLOPS", "megaFLOPS", "gigaFLOPS", "teraFLOPS", "petaFLOPS", 
                    "exaFLOPS", "zettaFLOPS", "yottaFLOPS"]
INFRA_TYPES = ["publicCloud", "privateCloud", "onPremise", "$other"]
POWER_SUPPLIER_TYPES = ["public", "private", "internal", "$other"]
POWER_SOURCES = ["solar", "wind", "nuclear", "hydroelectric", "gas", "coal", "$other"]
QUALITY_LEVELS = ["high", "medium", "low"]
HASH_ALGORITHMS = ["MD5", "RIPEMD-128", "RIPEMD-160", "RIPEMD-256", "RIPEMD-320", 
                  "SHA-1", "SHA-224", "SHA256", "SHA-384", "SHA-512"]
CRYPTO_ALGORITHMS = ["RSA", "DSA", "ECDSA", "EDDSA"]
CACHE_OPTIONS = ["true", "false"]