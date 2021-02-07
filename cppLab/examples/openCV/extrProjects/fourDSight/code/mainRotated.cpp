#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include <iostream>
using namespace std;
using namespace cv;


int main(){

  Mat img; 
  Mat templ; 
  Mat mask; 
  Mat result;
  Mat img_display;
  int match_method;

  double minVal; 
  double maxVal; 
  Point minLoc; 
  Point maxLoc;
  Point matchLoc;
  
  img = imread("StarMap_Original.jpg"),IMREAD_COLOR ;
  templ = imread("Small_area_rotated.jpg",IMREAD_COLOR );

  img.copyTo( img_display );
  

  int result_cols =  img.cols - templ.cols + 1;
  int result_rows = img.rows - templ.rows + 1;

  result.create( result_rows, result_cols, CV_32FC1 );
  
  match_method = 5; //TM COEFF NORMED
  matchTemplate( img, templ, result, match_method ); 
  imwrite("test.jpg", result );
  normalize( result, result, 0, 1, NORM_MINMAX, -1, Mat() );


  minMaxLoc( result, &minVal, &maxVal, &minLoc, &maxLoc, Mat() );

  matchLoc = maxLoc;

  //rectangle( img_display, matchLoc, Point( matchLoc.x + templ.cols , matchLoc.y + templ.rows ), Scalar(0,0,255), 2, 8, 0 );
  circle( img_display, Point( matchLoc.x , matchLoc.y ), 3, Scalar( 0, 255, 0 ), 3, 8 );
  circle( img_display, Point( matchLoc.x + templ.cols, matchLoc.y ), 3, Scalar( 0, 255, 0 ), 3, 8 );
  circle( img_display, Point( matchLoc.x , matchLoc.y + templ.rows), 3, Scalar( 0, 255, 0 ), 3, 8 );
  circle( img_display, Point( matchLoc.x + templ.cols, matchLoc.y + templ.rows), 3, Scalar( 0, 255, 0 ), 3, 8 );

  imshow("Rotated Image", img_display );
  imwrite("./cpp_small_area_rotated.jpg", img_display );

    return 0;
}
