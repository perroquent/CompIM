import os
import argparse
from PIL import Image
import torch
from torchvision import transforms
from torchvision.utils import save_image
from model import Model
from utils import extract_image_names_recursive
import time

trans = transforms.Compose([transforms.ToTensor()])


def main():
    parser = argparse.ArgumentParser(description='Multimodal Style Transfer by Pytorch')
    parser.add_argument('--content', '-c', type=str, default=None,
                        help='Content image path e.g. content.jpg')
    parser.add_argument('--style', '-s', type=str, default=None,
                        help='Style image path e.g. image.jpg')
    parser.add_argument('--output_name', '-o', type=str, default=None,
                        help='Output path for generated image, no need to add ext, e.g. out')
    parser.add_argument('--n_cluster', type=int, default=3,
                        help='number of clusters of k-means ')
    parser.add_argument('--alpha', default=1,
                        help='fusion degree, should be a float or a list which length is n_cluster')
    parser.add_argument('--lam', type=float, default=0.1,
                        help='weight of pairwise term in alpha-expansion')
    parser.add_argument('--max_cycles', default=None,
                        help='max_cycles of alpha-expansion')
    parser.add_argument('--gpu', '-g', type=int, default=0,
                        help='GPU ID(negative value indicate CPU)')
    parser.add_argument('--model_state_path', type=str, default='model_state.pth',
                        help='pretrained model state')

    args = parser.parse_args()

    # set device on GPU if available, else CPU
    if torch.cuda.is_available() and args.gpu >= 0:
        device = torch.device(f'cuda:{args.gpu}')
        print(f'# CUDA available: {torch.cuda.get_device_name(0)}')
    else:
        device = 'cpu'

    # set model
    model = Model(n_cluster=args.n_cluster,
                  alpha=args.alpha,
                  device=device,
                  lam=args.lam,
                  max_cycles=args.max_cycles)
    if args.model_state_path is not None:
        model.load_state_dict(torch.load(args.model_state_path, map_location=lambda storage, loc: storage))
        print(f'{args.model_state_path} loaded')
    model = model.to(device)


    content = args.content
    style = args.style

    content_batch = extract_image_names_recursive(content)
    style_batch = extract_image_names_recursive(style)

    count = 0
    for j in style_batch:
        for i in content_batch:
    
            c = Image.open(i)
            s = Image.open(j)
            c_tensor = trans(c).unsqueeze(0).to(device)
            s_tensor = trans(s).unsqueeze(0).to(device)

            with torch.no_grad():
                out = model.generate(c_tensor, s_tensor).to('cpu')

            c_name = os.path.splitext(os.path.basename(i))[0]
            s_name = os.path.splitext(os.path.basename(j))[0]
            args.output_name = f'{s_name}_{c_name}'

            save_image(out, f'test_result\{args.output_name}.jpg', nrow=1)
            """
            o = Image.open(f'{args.output_name}.jpg')

            demo = Image.new('RGB', (c.width * 2, c.height))
            o = o.resize(c.size)
            s = s.resize((i // 4 for i in c.size))

            demo.paste(c, (0, 0))
            demo.paste(o, (c.width, 0))
            demo.paste(s, (c.width, c.height - s.height))
            demo.save(f'result\{args.output_name}_style_transfer_demo.jpg', quality=95)

            o.paste(s,  (0, o.height - s.height))
            o.save(f'result\{args.output_name}_with_style_image.jpg', quality=95)
            """
            count += 1
            print(f'result saved into the "result" file starting with {args.output_name}')
            print(f"Iteration number {count}")
    return count

if __name__ == '__main__':
    
    start_time = time.time()
    count = main()
    difference = (time.time() - start_time)
    print("--- %s seconds ---" % difference)
    difference = int(difference)
    print(f"The process took {difference} seconds for {count} images. It's an average of {difference/count} sec per images.")