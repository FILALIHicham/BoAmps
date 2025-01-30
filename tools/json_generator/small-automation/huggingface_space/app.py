import gradio as gr
from services.huggingface import init_huggingface, update_dataset
from services.json_generator import generate_json
from ui.form_components import (
    create_header_tab,
    create_task_tab,
    create_measures_tab,
    create_system_tab,
    create_software_tab,
    create_infrastructure_tab,
    create_environment_tab,
    create_quality_tab,
    create_hash_tab
)

# Initialize Hugging Face
init_huggingface()

def handle_submit(*inputs):
    message, file_output, json_output = generate_json(*inputs)
    
    # Check if the message indicates validation failure
    if message.startswith("The following fields are required"):
        return message, file_output, json_output
    
    # If validation passed, proceed to update_dataset
    update_output = update_dataset(json_output)
    return update_output, file_output, json_output

# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Data Collection Form")
    gr.Markdown("Welcome to this Huggingface space that helps you fill in a form for monitoring the energy consumption of an AI model.")

    # Create form tabs
    header_components = create_header_tab()
    task_components = create_task_tab()
    measures_components = create_measures_tab()
    system_components = create_system_tab()
    software_components = create_software_tab()
    infrastructure_components = create_infrastructure_tab()
    environment_components = create_environment_tab()
    quality_components = create_quality_tab()
    hash_components = create_hash_tab()

    # Submit and Download Buttons
    submit_button = gr.Button("Submit")
    output = gr.Textbox(label="Output", lines=1)
    json_output = gr.Textbox(visible=False)
    file_output = gr.File(label="Downloadable JSON")

    # Event Handlers
    submit_button.click(
        handle_submit,  
        inputs=[
            *header_components,
            *task_components,
            *measures_components,
            *system_components,
            *software_components,
            *infrastructure_components,
            *environment_components,
            *quality_components,
            *hash_components
        ],
        outputs=[output, file_output, json_output]
    )

if __name__ == "__main__":
    demo.launch()