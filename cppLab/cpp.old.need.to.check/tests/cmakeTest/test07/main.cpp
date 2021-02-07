#include <iostream>
//#include <adder.h>
#include <GLFW/glfw3.h>
#include <EHEConfig.h>

#ifdef USE_ADDER
    #include <adder.h>
#endif

using namespace std;


int main(int argc, char* argv[]){
    
    cout<<"Hello"<<endl;

    #ifdef USE_ADDER
        //if USER_ADDER is ON in CMakeLists.txt
        cout << "Using Adder Lib : " << add(34.5f, 45.9f) << '\n';
    #else
        cout << "Not Using Adder Lib : " << 34.5f + 73.8f <<"\n";
    #endif

    cout << argv[0] << " - Version : " << EHE_VERSION_MAJOR << "." << EHE_VERSION_MINOR << "\n";
    GLFWwindow* window;
    int width, height;

    if( !glfwInit() )
    {
        fprintf( stderr, "Failed to initialize GLFW\n" );
        exit( EXIT_FAILURE );
    }

    window = glfwCreateWindow( 300, 300, "Gears", NULL, NULL );
    if (!window)
    {
        fprintf( stderr, "Failed to open GLFW window\n" );
        glfwTerminate();
        exit( EXIT_FAILURE );
    }



    // Main loop
    while( !glfwWindowShouldClose(window) )
    {
        /*
        // Draw gears
        draw();

        // Update animation
        animate();

        // Swap buffers
        */
        glfwSwapBuffers(window);
        glfwPollEvents();


    }

    // Terminate GLFW
    glfwTerminate();


    return 0;
}