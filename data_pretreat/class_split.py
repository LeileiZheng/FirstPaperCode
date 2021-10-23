import os
from shutil import copyfile

root_path = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
print(root_path)
data_path = os.path.join(root_path, "Isic_2018")
train_path = os.path.join(data_path, "train")
test_path = os.path.join(data_path, "test")
train_ground_truth_root = os.path.join(data_path, "Training_GroundTruth.csv")
train_source = "D:\\000\\000_the_first_paper\ISIC2018\Training_Input"


def makedir(path):
    """
    if path does not exist in the file system, create it
    """
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == '__main__':
    class_list = []
    with open(train_ground_truth_root) as f:
        # 读第一行
        first_line = f.readline().strip('\n').split(',')
        for folder in first_line[1:]:
            makedir(os.path.join(train_path, folder))
            class_list.append(folder)
        # 根据分类复制文件
        for line in f.readlines()[1:]:
            split = line.strip('\n').split(',')
            for i in range(len(class_list)):
                if split[i + 1] == '1.0':
                    copyfile(os.path.join(train_source, split[0] + '.jpg'),
                             os.path.join(train_path, class_list[i], split[0] + '.jpg'))
