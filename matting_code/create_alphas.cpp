#include "globalmatting.h"
#include "guidedfilter.h"

using namespace std;


string getFileName(int n){
    if(n < 10){
        return "0000" + std::to_string(n);
    }
    else{
        return "000"+std::to_string(n);
    }
}

int matting_helper(string fileName){
    string image_path = "car.png";
    string tripmap_path = "car-trimap.png";


    cv::Mat image = cv::imread(image_path, CV_LOAD_IMAGE_COLOR);
    cv::Mat trimap = cv::imread(tripmap_path, CV_LOAD_IMAGE_GRAYSCALE);

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

    cv::imwrite("../alpha_mattings/480p/car-turn/"+fileName+".png", alpha);

    return 0;

}

int main(){
    //Create alpha mattings for all trimaps 00000-00081
    // for(int i = 0; i <= 81; i++){
     matting_helper(getFileName(48));
    // }

    return 0;
}

