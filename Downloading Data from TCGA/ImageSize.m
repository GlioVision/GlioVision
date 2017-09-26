files = dir('C:/Research/APPatches/*.png');
fprintf("starting!_");
counter = 0;
a = 0;
for i = 1: length(files)
    totalName = strcat('C:/Research/APPatches/', files(i).name);
    img = imread(totalName);
    [height, width] = size(img);
    width = width/3;
    if((height ~= 256)||(width ~=256))
        counter = counter + 1;
        fprintf("\n ERROR: ");
        fprintf(totalName);
        fprintf(" NOT RIGHT SIZE.");
        fprintf(int2str(height));
        fprintf(" ");
        fprintf(int2str(width));
        fprintf(" COUNTER: ");
        fprintf(int2str(counter));
        fprintf('\n');
    end
    if(mod(a, 100) == 0)
        fprintf(int2str(a));
        fprintf('\t');
    end
    a = a + 1;
end
fprintf('\n\n\n\n\n');
fprintf(int2str(counter));