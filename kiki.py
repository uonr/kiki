#!/usr/bin/env python3
import os
import argparse
import tempfile
import math
parser = argparse.ArgumentParser(description='')
parser.add_argument('-f', '--file', default=None, required=False)
parser.add_argument('-t', '--time', help='timestamp in seconds', default='0', required=False)
parser.add_argument('-l', '--lang', help='language', default='auto', required=False)

args = parser.parse_args()

temp_dir = tempfile.mkdtemp()  # Create a temporary directory

input_filename = args.file
if input_filename == None:
    file_list = os.listdir("input")

    if len(file_list) == 0:
        print("Please add a flag -f to specify a file")
        exit(1)

    sorted_file_list = sorted(file_list, key=lambda x: os.path.getctime(os.path.join("input", x)))
    input_filename = 'input/' + sorted_file_list[-1]

if not os.path.exists(input_filename):
    print(f"Input file '{input_filename}' does not exist")
    exit(1)

audio_file = f"{temp_dir}/output.wav"

convert_command = f"ffmpeg -i '{input_filename}' -vn -ar 16000 -ac 1 -c:a pcm_s16le '{audio_file}'" 
try:
    print(convert_command)
    os.system(convert_command)
    offset_time = math.floor(float(args.time) * 1000)
    duration = 5 * 60 * 1000
    whisper_command = f'./whisper.cpp/main --processors 4 --threads 8 --language {args.lang} -m whisper.cpp/models/ggml-large-v3.bin -f {audio_file} --offset-t {offset_time} --duration {duration} --output-srt --output-file ./output'
    print(whisper_command)
    os.system(whisper_command)
finally:
    os.remove(audio_file)