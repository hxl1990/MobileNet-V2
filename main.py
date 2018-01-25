from model import MobileNetV2
from utils import parse_args, create_experiment_dirs


def main():
    # Parse the JSON arguments
    try:
        config_args = parse_args()
    except:
        print("Add a config file using \'--config file_name.json\'")
        exit(1)

    # Create the experiment directories
    _, config_args.summary_dir, config_args.checkpoint_dir = create_experiment_dirs(config_args.experiment_dir)

    model = MobileNetV2(config_args)

    if config_args.cuda:
        model.cuda()

    # Model Summary
    print(model)


if __name__ == "__main__":
    main()