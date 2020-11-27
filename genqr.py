#!/usr/bin/python3

import qrcode
import optparse

def generaQR(messaggio,file,dimensione,border,version,errorcorrectinglevel):
    qr = qrcode.QRCode(version=version,box_size=dimensione,border=border,error_correction=errorcorrectinglevel)
    qr.add_data(messaggio)
    qr.make(fit=True)
    img = qr.make_image(fill='black',back_color='white')
    img.save(file)


def Main():
    parser = optparse.OptionParser('Use: qrgen -m message -o outputfile [-w width] [-b border] [-v version] [-e errorcorrectinglevel]',version='%prog 1.0')
    parser.add_option('-m', dest='message',type='string',help='Message to save in the QR Code')
    parser.add_option('-o', dest='outputfile',type='string',help='Where to save the QR Code')
    parser.add_option('-w', dest='width',type='int',default=15,help='Number of pixels to get a block of information')
    parser.add_option('-b', dest='border',type='int',default=5,help='Border of the QR Code')
    parser.add_option('-v', dest='version',type='int',default=1,help='Version')
    parser.add_option('-e', dest='error',type='string',default='L',help='Error correcting level {L = 7%, M = 15%, Q = 25%, H = 30%}')
    (options, args) = parser.parse_args()
    if options.message == None or options.outputfile == None:
        print('Error! Use "genqr -h" to get help')
        exit(0)
    options.error = options.error.upper()
    if options.error == 'L':
        options.error = qrcode.constants.ERROR_CORRECT_L
    elif options.error == 'M':
        options.error = qrcode.constants.ERROR_CORRECT_M
    elif options.error == 'Q':
        options.error = qrcode.constants.ERROR_CORRECT_Q
    elif options.error == 'H':
        options.error = qrcode.constants.ERROR_CORRECT_H
    else:
        print('Error! Use "genqr -h" to get help')
        exit(0)
    generaQR(options.message,options.outputfile,options.width,options.border,options.version,options.error)

if __name__ == '__main__':
    Main()
