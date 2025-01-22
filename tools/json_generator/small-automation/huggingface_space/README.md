# AI Model Energy Consumption Data Collection Form

## Overview
This HuggingFace Space Gradio app provides an interactive form interface for monitoring and reporting the energy consumption of AI models. The application collects detailed information about model training, infrastructure, measurements, and environmental impact, storing the data in a structured format on Hugging Face datasets.

## Features
- Comprehensive data collection across multiple categories
- Automatic JSON generation and validation
- Direct integration with Hugging Face datasets
- User-friendly form interface built with Gradio

## Code Structure

- **`ui/form_components.py`**: Contains the Gradio components for each form tab.
- **`services/json_generator.py`**: Generates JSON data from the form inputs.
- **`services/huggingface.py`**: Handles the interaction with the Hugging Face dataset.
- **`config.py`**: Configuration file for Hugging Face token, dataset name, and form field options.
- **`app.py`**: Main application file that initializes the Gradio interface.
- **`utils/validation.py`**: Validates that all required fields are filled before submission.

## Setup Instructions

### 1. Create a Hugging Face Space
1. Go to [Hugging Face](https://huggingface.co)
2. Click on your profile picture and select "New Space"
3. Choose the following settings:
   - Owner: Your username or organization
   - Space name: Your preferred name
   - Select "Gradio" as the SDK
   - Choose license type
   - Make it public or private as needed

### 2. Configure Space Settings
1. Go to your Space's settings
2. Navigate to the "Variables" section
3. Add a new secret variable:
   - Name: `HF_TOKEN`
   - Value: Your Hugging Face write token (generate one from your [Hugging Face settings](https://huggingface.co/settings/tokens))

### 3. Link to Dataset
The application is configured to use a specific dataset. To change this:
1. Open `config.py`
2. Modify the `DATASET_NAME` variable to your desired dataset path:
```python
DATASET_NAME = "your-username/your-dataset-name"
```

### 4. Deploy Code
1. Clone your Space repository:
```bash
git clone https://huggingface.co/spaces/your-username/your-space-name
```

2. Copy all project files maintaining the directory structure, except the README.md you should keep the one from the Space:
```
.
├── .gitattributes
├── ui/
│   └── form_components.py
├── services/
│   ├── json_generator.py
│   └── huggingface.py
├── config.py
├── app.py
└── utils/
    └── validation.py
```

3. Push the changes:
```bash
git add .
git commit -m "Initial commit"
git push
```

## Usage
1. Access your Space through the Hugging Face interface
2. Fill out the form sections, especially the required fields
3. Click "Submit" to save the data
4. Download the generated JSON file if needed

## Dependencies
- gradio
- huggingface_hub
- datasets
- python>=3.7

## Authors

This gradio app for huggingface was initially coded by [Hicham Filali](https://github.com/FILALIHicham) but there is still room for improvement, Contributions are welcome!
