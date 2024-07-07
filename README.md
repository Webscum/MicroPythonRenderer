# Micro Python Renderer
This is a small 3D renderer with a modified MicroObjLoader (own) for storage optimization.

The modified MicroObjLoader doesn't account for vertex textures in the .obj file as they are not useful in a very resource tight and slow enviroment, it also calcultes the face normal from the vertex normals and uses that instead of doing it on the fly.

The unmodified version of [MicroObjLoader](https://github.com/Webscum/MicroObjLoader) is public on my profile.
