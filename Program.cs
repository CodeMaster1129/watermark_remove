using Emgu.CV;
using Emgu.CV.CvEnum;
using Emgu.CV.Structure;

// Load the original image
Mat originalImage = CvInvoke.Imread("image-with-watermark.jpg", ImreadModes.Color);

// Load the watermark-free image (or create one)
Mat watermarkFreeImage = CvInvoke.Imread("watermark_free.jpg", ImreadModes.Color);

// Ensure both images have the same size
CvInvoke.Resize(watermarkFreeImage, watermarkFreeImage, originalImage.Size);

// Blend the original image with the watermark-free image
double alpha = 0.5; // Adjust the alpha value to control the blending strength
Mat resultImage = new Mat();
CvInvoke.AddWeighted(originalImage, alpha, watermarkFreeImage, 1 - alpha, 0, resultImage);

// Save the result
CvInvoke.Imwrite("output.jpg", resultImage);


