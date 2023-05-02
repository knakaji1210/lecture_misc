import sys
from PIL import Image
import glob

args = sys.argv

if __name__ == '__main__':
    output_file_name = "./gif/"+args[1]+".gif"
    files = sorted(glob.glob('./png/*.png'))  
    images = list(map(lambda file : Image.open(file) , files))
    images[0].save(output_file_name , save_all = True , append_images = images[1:] , duration = 400 , loop = 0)
