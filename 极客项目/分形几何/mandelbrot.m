function index = mandelbrot(center, width, grid, depth)
    s = width*(-1:1/grid:1);
    [u,v] = meshgrid(s+real(center),s+imag(center));
    z0 = u + 1i*v;
    [row, ~] = size(z0);
    z = zeros(row);
    index = zeros(row);
    tic
    for ii = 1:depth
        z = z.^2 + z0;
        index(abs(z)<2) = ii;
    end
    toc
    image(index)
    axis image
    colormap(flipud(hot(depth)))
end