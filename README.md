# Micro Python Renderer

## General
  This is a small 3D renderer with a modified MicroObjLoader (own) for storage optimization.
  
  The modified MicroObjLoader doesn't account for vertex textures in the .obj file as they are not useful in a very resource tight and slow enviroment, it also calcultes the face normal from the vertex normals and uses that instead of doing it on the fly.
  
  The unmodified version of [MicroObjLoader](https://github.com/Webscum/MicroObjLoader) is public on my profile.
  
  Clipping is done via a simple dot product to see if an angle is 90 degrees, it isn't very refined or viable

## Parts info
  ### Screen
  - [Adafruit](https://www.adafruit.com/product/326)
  - [Datasheet](https://cdn-shop.adafruit.com/datasheets/SSD1306.pdf)
    
  ### Rotary Encoder
  - [Adafruit](https://www.adafruit.com/product/377)
  - [Datasheet](https://cdn-shop.adafruit.com/datasheets/pec11.pdf)
