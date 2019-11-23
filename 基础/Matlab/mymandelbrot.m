clear
clc

grid = 1024;
w = 2;
s = w*(-1:1/grid:1);
zc =-1 + 0.5*1i;
[u,v] = meshgrid(s+real(zc),s+imag(zc));

z0 = u + 1i*v;
z1 = gpuArray(u + 1i*v);
tic
kzgpu = arrayfun(@mandelbrot,z0);
toc

tic
kzcpu = arrayfun(@mandelbrot,z1);
toc

imagesc(kzcpu)


function kz = mandelbrot(z0)
    z = z0;
    kz = 0;
    depth = 255;
    while (z*conj(z) <= 4) && (kz <= depth)
        kz = kz + 1;
        z = z*z + z0;
    end
end