# MC Asset Generator


## Goals
- Generate assets for Minecraft
- Update Stable diffusion model to 3.5 or 3.0
- Improve asset quality and consistency using either LoRa, ControlNet, or IP-Adapters/other techniques
- Investigate Dreambooth as an option for training an alternative checkpoint model.
## Data
- 3,000 labeled images of varying quality of Minecraft textures



## Training & Usage of LoRa model.
To use the following you must have a GPU with at least 16GB of VRAM and 32GB of RAM locally. Or alternatively, use a cloud-based solution such as Google Colab or AWS SageMaker.
1. Download Stable Diffusion checkpoint model 2.1 as your foundational model. Or you can attempt to train the LoRa model for a different foundational model for varying results.
2. Use Kohya Trainer
