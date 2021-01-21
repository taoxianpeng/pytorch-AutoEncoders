import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
from torchvision.transforms.transforms import ToPILImage

class MyDataset():
    def __init__(self,path,img_size) -> None:
        self.path = path
        self.size = img_size
    def getDatasets(self,):
        transform = transforms.Compose([
            # transforms.ToPILImage(),
            transforms.Resize((self.size)), 
            transforms.ToTensor(), 
            #三通道rgb图片转单通道灰度图
            transforms.Grayscale(num_output_channels=1),
            transforms.Normalize(0.5, 0.5)
        ])
        datasets = ImageFolder(root = self.path, transform=transform)
        return datasets

# class MyDataset(Dataset):

#     def __init__(self, path):

#         self.img, self.target = MyDataset.load_data(path)

#         print(len(self.img), len(self.target))

#     @staticmethod
#     def load_data(path):
#         img_list = []
#         target_list = []
#         for root, dirs, files in os.walk(path):
#             for i, dir in enumerate(dirs):
#                 img_file = glob.glob(root+'/'+dir+'/'+'*.*')
#                 print("img_file: ", img_file)
#                 for img_ in img_file:
#                 m = Image.open(img_)

#                 transform = transforms.Compose([
#                     transforms.Resize((64, 64), interpolation=2),
#                     transforms.ToTensor(),
#                     transforms.Normalize(
#                         mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]),
#                 ])

#                 img_list.append(transform(m))
#                 target_list.append(i)

#         return img_list, target_list

#     def __getitem__(self, index):
#         return self.img[index], self.target[index]

#     def __len__(self):
#         return len(self.img)
