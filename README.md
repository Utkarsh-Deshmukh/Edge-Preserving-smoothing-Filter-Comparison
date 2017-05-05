# Edge-Preserving-smoothing-Filter-Comparison

Computational time vs quality comparison between some Edge preserving smoothing filters

Inorder to reduce gaussian noise, we usually want to smooth the image. But we do not want to smooth out the true edges in the image. Hence, we use Edge Preserving Smoothing filter. In this project, we do a time and quality comparison between "Bilateral Filter" and "Guided Filter". Future releases will include other techniques such as anisotropic diffusion and Kuwahara filters.

## Results

- Guided filters use integral image to perform smoothing (They use boxfiltering). Hence, the computational complexity is not dependant on the size of the smoothing kernel.
 The plot of "time required" vs "Kernel size" looks as follows:
![time_comparison](https://cloud.githubusercontent.com/assets/13918778/25735656/b5a0bbd0-3121-11e7-85db-fb79a3469a23.png)

Here is a quality comparison between the two: (Note: you can get a better quality by playing around the sigma_space and sigma_color parameters in the bilateral filter and the "radius" and "eps" parameter in guided filter)
 
![graphics](https://cloud.githubusercontent.com/assets/13918778/25735611/8baad20c-3121-11e7-87d4-cd2b1ebc26eb.gif)


## Dependencies
- python
- opencv
- numpy 

## Implementation

- go to the folder "src"
- run the following command
  
  python main.py
  
## License
- This project is licensed under the BSD 2 License - see the LICENSE.md file for details

## Acknowledgements

The guided filter code is based on the implementation of Kaiming He (Reference Paper: Fast Guided Filter, https://arxiv.org/abs/1505.00996).

The Bilateral filter code is used from a built in implementation in opencv
