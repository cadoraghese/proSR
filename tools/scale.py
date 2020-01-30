from argparse import ArgumentParser
from math import floor, ceil
from PIL import Image


def downscale_by_ratio(img, ratio, method=Image.BICUBIC, magic_crop=False):
    if ratio == 1: return img

    w, h = img.size
    if magic_crop:
        img = img.crop((0, 0, w - w % ratio, h - h % ratio))
        w, h = img.size

    w, h = floor(w / ratio), floor(h / ratio)
    return img.resize((w, h), method)


def downscale_by_size(img, size, method=Image.BICUBIC):

    min = 64
    magic = size // min
    w, h = img.size
    max_dim = max(w, h)
    factor = max_dim / size
    w, h = round(w / factor / magic) * magic, round(h / factor / magic) * magic
    return img.resize((w, h), method)


def parse_args():
    parser = ArgumentParser(description='Downscale')
    parser.add_argument('-i', '--input', help='Input image')
    parser.add_argument('-o', '--output', help='Output imag.')

    parser.add_argument(
        '-r',
        '--ratio',
        help='scale ratio e.g. 2, 4 or 8',
        type=int,
        required=False)

    parser.add_argument(
        '-mx',
        '--max_size',
        help='Max size',
        type=int,
        required=False)

    args = parser.parse_args()

    return args


def main(args):

    import os
    isFile = os.path.isfile(args.input)
    isDirectory = os.path.isdir(args.input)

    if isDirectory and not os.path.exists(args.output):
        os.system('mkdir ' + args.output)

    if isFile:
        img = Image.open(args.input)
        if args.ratio:
            img_scaled = downscale_by_ratio(img, args.ratio)
        if args.max_size:
            img_scaled = downscale_by_size(img, args.max_size)

        img_scaled.save(args.output)

    if isDirectory:
        for file in os.listdir(args.input):
            img = Image.open(args.input + file)
            if args.ratio:
                img_scaled = downscale_by_ratio(img, args.ratio)
            if args.max_size:
                img_scaled = downscale_by_size(img, args.max_size)

            img_scaled.save(args.output + file)


if __name__ == '__main__':
    # Parse command-line arguments
    args = parse_args()
    main(args)
