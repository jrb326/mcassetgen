# MC Asset Generator


## Goals
- Generate assets for Minecraft
- Create a programmatic script for training the LoRa model and running inference using pytorch.
- Update Stable diffusion model to 3.5 or 3.0
- Improve asset quality and consistency using either LoRa, ControlNet, or IP-Adapters/other techniques
- Investigate Dreambooth as an option for training an alternative checkpoint model.
## Data
- 3,000 labeled images of varying quality of Minecraft textures



## Training & Usage of LoRa model.
To use the following you must have a GPU with at least 16GB of VRAM and 32GB of RAM locally. Or alternatively, use a cloud-based solution such as Google Colab or AWS SageMaker.
1. Download Stable Diffusion checkpoint model 2.1 as your foundational model. Or you can attempt to train the LoRa model for a different foundational model for varying results. Note: Kohya SS will have V2.1 able to be auto-downloaded as well.
2. Download Kohya SS to your local machine.
3. Once the LoRa model is trained through Kohya SS, you then get a model file.
4. To use the model, the easiest way will be through ComfyUI or Automatic1111, which will allow you to easily connect the model to Stable Diffusion.
5. Generate assets for Minecraft using the trained LoRa model!
