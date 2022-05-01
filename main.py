import time
import serial
import serial.tools.list_ports as port_list
from PIL import Image

serialPort_pc = serial.Serial(port="COM5", baudrate=9600, bytesize=8, timeout=None, stopbits=serial.STOPBITS_ONE)


def list_ports():
    """
    The function that list and print the available comports of computer.
    :return: List of Comports
    """
    ports = list(port_list.comports())
    for p in ports:
        print(p)
    return ports


def import_image():
    """
    import the image file
    :return:
    """
    img = Image.open('parrot_lowres.png')  # Can be many different formats.
    pix = img.load()
    pix_size = img.size
    # pix[x, y] = value
    # im.save('alive_parrot.png')  # Save the modified pixels as .png
    return pix, pix_size


def gray_scale(pix, pix_size):
    """
    :param pix: input picture
    :param pix_size: size of the picture
    :return: gray scale of picture
    """
    img2 = Image.new('RGB', pix_size)
    pix_gray = img2.load()
    # print(pix_size)
    # print("x = {} y = {}".format(pix_size[0], pix_size[1]))
    # print("x = {} y = {}".format(pix_size[0], pix_size[1]))
    for x in range(pix_size[0]):
        for y in range(pix_size[1]):
            pix_gray[x, y] = uart_fpga(pix[x, y])
    img2.save('gray_scale2.png')


def uart_fpga(rgb_value):
    """
    sends rgb values to fpga and receive the average value of that pixel
    :param rgb_value: rgb value of pixel
    :return:
    """
    # rgb_values = bin(rgb_value[0]) + bin(rgb_value[1]) + bin(rgb_value[2])
    rgb_values = format(rgb_value[0], '08b') + format(rgb_value[1], '08b') + format(rgb_value[2], '08b')
    print("rgb value {} => rgb binary: {}".format(rgb_value, rgb_values))
    serialPort_pc.write(str.encode(rgb_values))
    time.sleep(0.05)
    average = serialPort_pc.read(8)
    average_int = int(average, 2)
    gray_scale_pixel = (average_int, average_int, average_int)
    # print("{} type : {}".format(gray_scale_pixel,type(gray_scale_pixel)))
    return gray_scale_pixel


if __name__ == '__main__':
    list_ports()
    pix, pix_size = import_image()
    gray_scale(pix, pix_size)
