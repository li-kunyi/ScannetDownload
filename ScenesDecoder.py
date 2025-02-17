import argparse
import os, sys

from SensorData import SensorData


def main():
    dir_path = '/mnt/nfs-user/datasets/scans'
    items = os.listdir(dir_path)

    idx = 0

    for item in items:
        item_path = os.path.join(dir_path, item)
        idx += 1
        if os.path.isdir(item_path) and (idx > 74) and (idx <= 100) and \
            item != 'scene0001_00' and \
            item != 'scene0001_01' and \
            item != 'scene0003_00' and \
            item != 'scene0003_01' and \
            item != 'scene0003_02':

            filename = item_path + '/' + item + '.sens'
            
            sys.stdout.write('proceeding number %d file' % idx)
            print(filename)
            
            # load the data
            sys.stdout.write('loading %s...' % filename)
            sd = SensorData(filename)
            sys.stdout.write('loaded!\n')

            sd.export_depth_images(os.path.join(item_path, 'depth'))
            sd.export_color_images(os.path.join(item_path, 'color'))
            sd.export_poses(os.path.join(item_path, 'pose'))
            sd.export_intrinsics(os.path.join(item_path, 'intrinsic'))

            os.remove(filename)


if __name__ == '__main__':
    main()