# Data

## This is the raw images before upscaling
This information has been taken from various minecraft mods, and can be obtained by going to [Modrinth](https://modrinth.com/mods) or [CurseForge](https://www.curseforge.com/minecraft/mc-mods), downloading mods, and extracting the images from the JAR files.

## How to use this Data
This is the raw data, in ../image/ there exists two folders, which are supposed to be used for training. These images have been upscaled, and formatted to a uniform size (512 x 512) and (256 x 256) for training purposes. There are approximately 3k images. They have also had their backgrounds removed and are ready for training.

Within your TOML configuration for kohya_ss r SD-scripts for training Stable Diffusion 3.5 Large - you can specify these folders, like the example below. With that - the SD-scripts will grab the image folders and use them for training.

```TOML
[general]
# define common settings here
flip_aug = true
color_aug = false
keep_tokens_separator= "|||"
shuffle_caption = false
caption_tag_dropout_rate = 0
caption_extension = ".txt"

[[datasets]]
# define the first resolution here
batch_size = 1
enable_bucket = true
resolution = [512, 512]

  [[datasets.subsets]]
  image_dir = "/home/jupyter-jrb326/image/2_minecraft"
  num_repeats = 2

[[datasets]]
# define the second resolution here
batch_size = 1
enable_bucket = true
resolution = [256, 256]

  [[datasets.subsets]]
  image_dir = "/home/jupyter-jrb326/image/5_minecraft"
  num_repeats = 3
```
