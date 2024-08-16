
# OpenGL 3D Engine in Python

## Description

This project is a simple 3D engine built using Python and OpenGL. It allows rendering and manipulating 3D models within a Python environment. The engine supports loading and displaying various 3D mesh objects and provides basic functionalities such as camera movement and object transformation.

## Installation

To run this project, you need to have Python installed along with the necessary dependencies. The key dependencies are as follows:

- **PyOpenGL**: A cross-platform Python binding to OpenGL.
- **GLUT**: A utility toolkit for handling windowing and input.

You can install the dependencies using pip:

\`\`\`bash
pip install PyOpenGL PyOpenGL_accelerate
\`\`\`

Additionally, you might need a tool to view the 3D window created by GLUT.

## Usage

After installing the dependencies, you can run the engine using the \`main.py\` script. The engine includes several 3D models that you can load and manipulate.

To start the engine, run:

\`\`\`bash
python main.py
\`\`\`

## Files and Directories

- **\`Camera.py\`**: Contains the Camera class responsible for handling camera movements and perspectives within the 3D environment.
- **\`Cube.py\`**: Defines a simple Cube class that can be used to create and render cube objects.
- **\`LoadMesh.py\`**: A utility to load and process 3D mesh files in \`.obj\` format.
- **\`Mesh.py\`**: Defines the Mesh class for handling 3D models and their associated data.
- **\`main.py\`**: The entry point of the engine. It initializes the engine and loads the 3D models for rendering.
- **\`Engine/\`**: A subdirectory that contains additional Python files and 3D models.

These models are loaded and rendered by the engine to demonstrate its capabilities.
