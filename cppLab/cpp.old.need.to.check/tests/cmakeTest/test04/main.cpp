#include <iostream>
#include <adder.h>
#include <GLFW/glfw3.h>

using namespace std;


int main(){
    cout<<"Hello"<<endl;
    cout << add(34.5f, 45.9f) << '\n';

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