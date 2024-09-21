<br>

[Youtube Tutorial]()<br>
[Downloads](#-downloads)<br>
[Setup](#-setup)<br>
[How to use](#-how-to-use)<br>
[Documentation](#-documentation)<br>
[Examples](#-examples)<br>
[Subtitles](#-subtitles)<br>

## Installation Guide 📖


#### Downloads

Clone/download [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN.git)<br>

Download and install [Anaconda](https://www.anaconda.com/download/success)<br>

Make sure to download [Full Version](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z) of ffmpeg<br>

(Optional): Add ffmpeg to Path Environment, Useful for manipulating video files

#### Setup

1. Open an anaconda prompt and navigate to where you downloaded Real-ESRGAN:

    ```bash
    cd {path to your real-esrgan repo}
    ```

2. Then create and activate the environment:
    ```bash
    conda create -n real python=3.11.7
    conda activate real
    ```

<br><br>

3. Now we need to set up some dependencies: **(Important to follow the order)**
    ```bash
    pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121
    pip install chardet basicsr ffmpeg-python
    conda install ffmpeg
    pip install -r requirements.txt
    python setup.py develop
    ```

<br><br>


4. After that go to where you installed Anaconda:<br>
    ```bash
    {path to Anaconda3}\envs\real\Lib\site-packages\basicsr\data\
    ```
    Open the file named `degradations.py` with a text editor then find and replace the following line`8`:
   
    ```bash
    torchvision.transforms.functional_tensor => torchvision.transforms.functional
    ```


<br><br>

5. Navigate to where you downloaded ffmpeg and **copy everything** from the full ffmpeg bin directory:
    ```bash
    {path to ffmpeg}\bin\
    ```
    **Paste and Replace** ffmpeg files in the pkg files here:

    ```bash
    {path to Anaconda3}\pkgs\ffmpeg-6.1.1-gpl_h66c0b5b_108\Library\bin\
    ```

<br><br>

6. Finally, Add `func.py` and `inference_realesrgan_video_fast.py` files from this repo to your Real_ESRGAN directory<br><br>`inference_realesrgan_video_fast.py` is a modified version of the original file `inference_realesrgan_video.py` with code enhancements to speed up video processing speed.<br>`func.py` is a little utility I made to make the process easier and more simple.<br><br>Optionally you can also add the `snippets.txt` which contains some useful code snippets that you can copy and paste into Anaconda prompt to quickly run the process.

<br>


## How to use ⚡

Inside your Real-ESRGAN folder, Find the `inputs` folder, Place the files you want to upscale inside

Copy and paste the following lines in an anaconda prompt to start processing all the files in the inputs directory quickly
    
```bash
cd {path to your real-esrgan folder}
conda activate real
python func.py
```

If you have your repository stored on a drive other than the one windows is installed on,
Then remember to add a line to the start to boot into that drive for example:

```bash
d:
cd {path to your real-esrgan folder}
conda activate real
python func.py
```

<br><br>

If you want to process specific files or apply specific settings for each file then you can add lines in a note pad with customization for each file like the example below, then copy and paste it into anaconda:

```bash
python func.py -i inputs/myvideofile1.mp4 -n RealESRGAN_x4plus
python func.py -i inputs/myvideofile2.mp4 -o result_videos
python func.py -i inputs/myvideofile3.mp4 --suffix 4k
python func.py -i inputs/myvideofile4.mp4 -s 4
python func.py -i inputs/myvideofile5.mp4
```

<br><br>

`func.py` is just a helper tool to make the process easier and more accessible, If you wish for more control then you can make lines that call the inference files directly:

```bash
# calling the inference_realesrgan_video_fast directly
python inference_realesrgan_video_fast.py -n realesr-animevideov3 -i inputs/myvideo.mp4 -o results -s 2 --link --suffix fast_4k

# calling the original inference_realesrgan_video directly
python inference_realesrgan_video.py -n realesr-animevideov3 -i inputs/myvideo.mp4 -o results -s 3 --suffix default_4k
```

<br>

## Documentation

`func.py` has a few arguments that allow you to customize the behaviour

    Usage: python func.py [options]...
    
        -h --help                   show this help message and exit

        -i --input                  Specify the input file/directory, Default: inputs
        
        -o --output                 Specify the output directory, Default: results
        
        -s --outscale               The final upsampling scale of the image, Default: 2
    
        -n --model_name             Model names: realesr-animevideov3 | RealESRGAN_x4plus_anime_6B | RealESRGAN_x4plus |
                                    RealESRNet_x4plus | RealESRGAN_x2plus | realesr-general-x4v3Default:realesr-animevideov3
        
        -sf --suffix                Suffix added to end of the output file, Default: 4k
        
        -dm --dont_move             Stops the file from moving to the done folder, Useful if you are planning to process the same
                                    file multiple times, or if you just dont like this behaviour
        
        -da --disable_audio         Do not include audio stream in result
        
        -ds --disable_subtitles     Do not include subtitle stream in result

### Examples

    # specify custom input or output 
    python func.py -i A:/real/inputs/video              # folder
    python func.py -i inputs/myVideo.mp4                # file (partial paths will search inside the project directory)
    python func.py -i inputs/myVideo.mp4 -o my_results  # file with output
    
    
    # specify custom scale
    python func.py -s 4
    
    # specify custom model
    python func.py -n RealESRNet_x4plus
    
    # specify custom suffix
    python func.py -sf 4k_result
    
    # stop file moving location after process is done
    python func.py -dm

    # do not include audio track in result
    python func.py -da
    
    # do not include subtitle track in result
    python func.py -ds


## Subtitles

The code for Subtitles is quite experimental and will likely break, it's honestly best to disable it `-ds` and find another way to extract the subtitles from the original work and add it to the 4k result





<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
















