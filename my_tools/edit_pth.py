from argparse import ArgumentParser
import torch


def parse_args():
    parser = ArgumentParser(
        description='Edit configuration file of the pretrained model.')
    parser.add_argument(
        'input', help='path to checkpoint', type=str)
    parser.add_argument(
        'output', help='path to new checkpoint', type=str)

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    # Parse command-line arguments
    args = parse_args()

    params_dict = torch.load(args.input)
    params_dict['params'].train.dataset.path.source = 'data/datasets/open_image/general_400_32'
    params_dict['params'].train.dataset.path.target = 'data/datasets/open_image/general_400_256'
    params_dict['params'].train.epochs = 275
    #params_dict['params'].train.lr_schedule_patience = 2
    params_dict['params'].train.io.save_model_freq = 5
    params_dict['params'].train.io.eval_epoch_freq = 1
    params_dict['params'].train.io.print_errors_freq = 40
    params_dict['params'].data.scale = [2, 4, 8]
    params_dict['params'].data.input_size = [48, 36, 24]
    torch.save(params_dict, args.output)
