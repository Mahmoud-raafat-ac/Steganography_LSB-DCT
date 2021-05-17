import numpy
import cv2
import xlwt

#MSE--start
def meanSquareError(img1, img2):
    error = numpy.sum((img1.astype('float') - img2.astype('float')) ** 2)
    error /= float(img1.shape[0] * img1.shape[1])
    return error
#MSE--end

#PSNR--start
def PSNR(img1, img2):
    mse = meanSquareError(img1,img2)
    if mse == 0:
        return 100
    return 10 * numpy.log10( numpy.square(255) / mse )
#PSNR--end

#comparison and write xls
original = cv2.imread('test.png') #put your img
lsbEncoded = cv2.imread('LSB_test.png') #put your img
dctEncoded = cv2.imread('DCT_test.png') #put your img

book = xlwt.Workbook()
sheet1=book.add_sheet("Sheet 1")
style_string = "font: bold on , color red; borders: bottom dashed"
style = xlwt.easyxf(style_string)
sheet1.write(0, 0, "Original vs", style=style)
sheet1.write(0, 1, "MSE", style=style)
sheet1.write(0, 2, "PSNR", style=style)
sheet1.write(1, 0, "LSB")
sheet1.write(1, 1, meanSquareError(original, lsbEncoded))
sheet1.write(1, 2, PSNR(original, lsbEncoded))
sheet1.write(2, 0, "DCT")
sheet1.write(2, 1, meanSquareError(original, dctEncoded))
sheet1.write(2, 2, PSNR(original, dctEncoded))

book.save("Comparison.xls")
print("Comparison Results were saved as xls file!")
#end
