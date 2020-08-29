import os
import argparse
import typing

from pydub import AudioSegment

def import_clips(files, directory: list, format: str, framerate: int) -> dict:
    clips = {}
    for filename in files:
        clips[filename] = AudioSegment.from_file(directory+'/'+filename, format=format, framerate=framerate)
    
    return clips

def segment_clips(clips: dict, clip_length: int, output, format: str) -> dict:
    segmented = {}
    if output is not None:
        file_num = 0
    for filename, clip in clips.items():
        if output is None:
            segmented.update({filename[:-4]+str(seg_clip[0])+'.'+format: seg_clip[1] for seg_clip in enumerate(clip[::clip_length])})
        else:
            segmented.update({output+str(file_num)+'_'+str(seg_clip[0])+'.'+format: seg_clip[1] for seg_clip in enumerate(clip[::clip_length])})
            file_num += 1
    
    return segmented
    
def main(args):
    clips = import_clips(os.listdir(args.directory), args.directory, args.input_format, int(args.framerate))
    segmented = segment_clips(clips, args.clip_length*1000, args.prefix, args.output_format)

    for filename, segment in segmented.items():
        with open(filename, 'wb') as sound:
            segment.export(sound, format=args.output_format)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Segment audio clips into smaller segments of themselves.')
    parser.add_argument('--directory', '-d', default='./', help='Use this argument to specify the directory that contains the clips you want segmented. If not specified, the current directory is attempted.')
    parser.add_argument('--clip_length', '-c', default='10', type=int, help='Use this argument to specify the length of the output clips. Specify time in seconds. If not specified, the default is 10 seconds.')
    parser.add_argument('--framerate', '-f', default=44100, type=int, help='Use this argument to specify the framerate the audio should be imported with. The default is 44100 Hz.')
    parser.add_argument('--input_format', '-I', default='mp3', help='Use this argument to specify the input file format. mp3, wav, etc. Default is mp3.')
    parser.add_argument('--output_format', '-O', default='mp3', help='Use this argument to specify the output file format. mp3, wav, etc. Default is mp3.')
    parser.add_argument('--prefix', '-p', default=None, help='Use this argument to specify the prefix of outputted clips. The default is the name of the filename.')
    main(parser.parse_args())
