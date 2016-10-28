#include "globalmatting.h"

// you can get the guided filter implementation
// from https://github.com/atilimcetin/guided-filter
#include "guidedfilter.h"
#include <opencv2/opencv.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>

int main(){
    for(int x = 0; x <= 81; x++){
        matting_helper(x);
    }
    return 0;
}
int toDoubleDigitString(int n){
    if(n < 10){
        return "0" + std::to_string(n);
    }
    else{
        return std::to_string(n);
    }
}
void matting_helper(int n)
{
    Mat dilated_image;
    Mat eroded_image;
    Mat dif;
    Mat trimap;
    Size s;

    std::string image_bw = "Masks/480p/bvs/bear/000" + toDoubleDigitString(x) + ".png";
    std::string image_ouput = "Masks/480p/bvs/bear/000" + toDoubleDigitString(x) + "_alpha.png";
    Mat image = cv::imread(image_bw, CV_LOAD_IMAGE_COLOR);
    dilate(image, dilated_image, Mat(), iterations=3);
    erode(image, eroded_image, Mat(), iterations=3);
    dif = dilute - erode;
    s = dif.size();
    for(int i = 0; i <= s.height; i++){
        for(int j = 0; j <= s.width; j++){
            if(dif.at<uchar>(i,j) > 0 && image<uchar>(i,j) == 0){
                trimap.at<uchar>(i,j) = 128; 
            } else if(dif.at<uchar>(i,j) > 0 && image<uchar>(i,j) > 0){
                trimap.at<uchar>(i,j) = 255;
            } else{
                trimap.at<uchar>(i,j) = 0;
            }
        }
    }
    // (optional) exploit the affinity of neighboring pixels to reduce the
    // size of the unknown region. please refer to the paper
    // 'Shared Sampling for Real-Time Alpha Matting'.
    expansionOfKnownRegions(image, trimap, 9);

    cv::Mat foreground, alpha;
    globalMatting(image, trimap, foreground, alpha);

    // filter the result with fast guided filter
    alpha = guidedFilter(image, alpha, 10, 1e-5);
    for (int x = 0; x < trimap.cols; ++x)
        for (int y = 0; y < trimap.rows; ++y)
        {
            if (trimap.at<uchar>(y, x) == 0)
                alpha.at<uchar>(y, x) = 0;
            else if (trimap.at<uchar>(y, x) == 255)
                alpha.at<uchar>(y, x) = 255;
        }

    cv::imwrite(image_ouput, alpha);

    
}