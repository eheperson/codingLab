/*
	To compile :
		step 1 :     g++ cpp_opencv_test.cpp -o cpp_opencv_test `pkg-config --cflags --libs opencv4`
		step 2 :     ./cpp_opencv_test
*/


#include <opencv2/highgui.hpp>
#include <iostream>
 
int main( int argc, char** argv ) {
  
  cv::Mat image;
  image = cv::imread("sample.jpg" , cv::IMREAD_COLOR);
  
  if(! image.data ) {
      std::cout <<  "Could not open or find the image" << std::endl ;
      return -1;
    }
  
  cv::namedWindow( "Display window", cv::WINDOW_AUTOSIZE );
  cv::imshow( "Display window", image );
  
  cv::waitKey(0);
  return 0;
}
