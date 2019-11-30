clear
clc

center =0.5 - 0*1i;
grid = 1024;
width = 3;
depth = 512;

s = width*(-1:1/grid:1);
[u,v] = meshgrid(s+real(center),s+imag(center));

z0 = u + 1i*v;
[r, c] = size(z0);
depth_0 = depth*ones(r, c);

z1 = gpuArray(z0);
depth_1 = gpuArray(depth_0);
tic
kzgpu = arrayfun(@mandelbrot,z1,depth_1);
toc


% tic
% kzcpu = arrayfun(@mandelbrot,z0, depth_0);
% toc

image(kzgpu)
axis image
colormap(flipud(jet(512)))


function kz = mandelbrot(z0, depth)
    z = z0;
    kz = 0;
    while (z*conj(z) <= 4) && (kz <= depth)
        kz = kz + 1;
        z = z*z + z0;
    end
end