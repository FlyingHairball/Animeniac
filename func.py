import os
import argparse
import subprocess
import mimetypes
import glob

# you can modify the behaviour of the script with these argument
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, default='inputs', help='Specify the input file/directory, Default: inputs')
parser.add_argument('-o', '--output', type=str, default='results', help='Specify the output directory, Default: results')
parser.add_argument('-s', '--outscale', type=float, default=2, help='The final upsampling scale of the image, Default: 2')
parser.add_argument('-n', '--model_name', type=str, default='realesr-animevideov3', help=('Model names: realesr-animevideov3 | RealESRGAN_x4plus_anime_6B | RealESRGAN_x4plus | RealESRNet_x4plus |'
              ' RealESRGAN_x2plus | realesr-general-x4v3'
              'Default:realesr-animevideov3'))
parser.add_argument('-sf', '--suffix', type=str, default='4k', help='Suffix added to end of the output file, Default: 4k')
parser.add_argument('-dm', '--dont_move', action='store_true', help='Stops the file from moving to the done folder, Useful if you are planning to process the same file multiple times, or if you just dont like this behaviour')
parser.add_argument('-da', '--disable_audio', action='store_true', help='Do not include audio stream in result')
parser.add_argument('-ds', '--disable_subtitles', action='store_true', help='Do not include subtitle stream in result')
args = parser.parse_args()
isFolder = mimetypes.guess_type(args.input)[0] == None


with open('batch.bat', 'w') as f:
    # handle folder input
    if isFolder:
        # create a folder to store the original files in after the process is done
        f.write(f'mkdir "{os.path.normpath(args.input)}\done"\n')

        # process every file in the folder
        paths = glob.glob(os.path.join(args.input, '*'))
        for path in paths:
            # skip folders
            if mimetypes.guess_type(path)[0] == None:
                continue
            # handle images
            elif mimetypes.guess_type(path)[0].startswith('image'):
                f.write(f'python inference_realesrgan.py -n {args.model_name} -i "{path}" -o "{args.output}" -s {args.outscale} --suffix {args.suffix}\n')
                if not args.dont_move:
                    f.write(f'move "{path}" "{args.input}\done"\n')
            # handle video
            elif mimetypes.guess_type(path)[0].startswith('video'):
                f.write(f'python inference_realesrgan_video_fast.py -n {args.model_name} -i "{path}" -o "{args.output}" -s {args.outscale} --link --suffix {args.suffix} {"--disable_audio" if args.disable_audio else ""} {"--disable_subtitles" if args.disable_subtitles else ""}\n')
                if not args.dont_move:
                    f.write(f'move "{path}" "{args.input}\done"\n')

    # handle single file input
    else:
        output_dir = os.path.normpath(os.path.dirname(args.input))
        f.write(f'python inference_realesrgan_video_fast.py -n {args.model_name} -i "{args.input}" -o "{args.output}" -s {args.outscale} --link --suffix {args.suffix}\n')
        f.write(f'mkdir "{output_dir}\done"\n')
        if not args.dont_move:
            f.write(f'move "{os.path.normpath(args.input)}" "{output_dir}\done"\n')

p = subprocess.Popen("batch.bat")
stdout, stderr = p.communicate()
