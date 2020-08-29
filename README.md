# segment-audio-clips
A simple command-line script to segment audio clips with a number of options, utilizing the [pydub](https://github.com/jiaaro/pydub) package. The system will output the clips in the current directory.<br>
Note: If using MacOS, the current system will fail unless ```.DS_Store``` files are removed from whatever directory the system is being run on.

## System Requirements
- Python 3.7+
- pydub 0.24.1+
- ffmpeg

## Using the System
```
python3 segment_clips.py [--directory, -d directory_name] [--clip_length, -c length] [--framerate, -f rate] [--input_format, -I format] [--output_format, -O format] [--prefix, -p prefix]
```
- ```--directory``` allows you to specify the directory that script should look for audio in. By default it will attempt the current directory.
- ```--clip_length``` allows you to specify the length of the clips you want to be output. By default the system outputs clips of 10 seconds.
- ```--framerate``` allows you to specify the framerate the audio should be input as. The default is 441000Hz.
- ```--input_format``` allows you to specify the format the audio should be input as. The default is mp3.
- ```--output_format``` allows you to specify the format the audio should be output as. The default is mp3.
- ```--prefix``` allows you to speficy the prefix of the ouputted files. For examples if ```test``` were specified, the output would be ```test0_0.mp3, test0_1.mp3...test3_1.mp3...```
