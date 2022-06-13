import cv2
import matplotlib.pyplot as plt
import torchstain
import torch
from torchvision import transforms
import time
import os
import argparse

parser = argparse.ArgumentParser(description='original data to voc text')
parser.add_argument('--target', type=str, default=None, metavar='N',
                    help='target file path')
parser.add_argument('--input', type=str, default=None, metavar='N',
                    help='input filer name')
parser.add_argument('--output', type=str, default=None, metavar='N',
                    help='output filer name')

def main():            
    args = parser.parse_args()       
    target = cv2.resize(cv2.cvtColor(cv2.imread(args.target), cv2.COLOR_BGR2RGB), (1716, 942))
    for imgs_path in os.listdir(args.input):
        to_transform = cv2.resize(cv2.cvtColor(cv2.imread(args.input+'/'+imgs_path), cv2.COLOR_BGR2RGB), (1716, 942))

        normalizer = torchstain.MacenkoNormalizer(backend='numpy')
        normalizer.fit(target)

        T = transforms.Compose([
            transforms.ToTensor(),
            transforms.Lambda(lambda x: x*255)
        ])

        torch_normalizer = torchstain.MacenkoNormalizer(backend='torch')
        torch_normalizer.fit(T(target))

        tf_normalizer = torchstain.MacenkoNormalizer(backend='tensorflow')
        tf_normalizer.fit(T(target))

        t_to_transform = T(to_transform)

        t_ = time.time()
        # norm, H, E = normalizer.normalize(I=to_transform, stains=True)
        # print("numpy runtime:", time.time() - t_)

        norm, H, E = torch_normalizer.normalize(I=t_to_transform, stains=True)
        print("torch runtime:", time.time() - t_)
        # plt.figure()
        # plt.suptitle('tensorflow normalizer')
        # plt.subplot(2, 2, 1)
        # plt.title('Original')
        # plt.axis('off')
        # plt.imshow(to_transform)

        # plt.subplot(2, 2, 2)
        # plt.title('Normalized')
        # plt.axis('off')
        # print(norm.shape)
        plt.figure(figsize=(23.19, 12.75), dpi=74)
        plt.axis("off")
        plt.imshow(norm)
        plt.savefig(args.output+'/'+imgs_path,bbox_inches='tight', format='png',pad_inches=0,dpi=96, transparent=True)
        plt.close()
        # plt.subplot(2, 2, 3)
        # plt.title('H')
        # plt.axis('off')
        # plt.imshow(H)

        # plt.subplot(2, 2, 4)
        # plt.title('E')
        # plt.axis('off')
        # plt.imshow(E)
        # plt.show()
        # save_norm = norm.cpu().numpy()
        # cv2.imwrite("./output/"+imgs_path, save_norm)


if __name__ == '__main__':
    main()

# t_ = time.time()
# norm, H, E = tf_normalizer.normalize(I=t_to_transform, stains=True)
# print("tf runtime:", time.time() - t_)


