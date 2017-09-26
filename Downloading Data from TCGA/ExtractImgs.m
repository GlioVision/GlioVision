files = dir('C:/Research/SVSFiles/*.svs');
for i = 1: length(files)
    folderName = files(i).name(1:end-4);
    SVSname = files(i).name;
    SVSname = strcat('C:/Research/SVSFiles/', SVSname);
    folderName = strcat('C:/Research/SVS/', folderName);
    if exist(folderName) ~= 7
        fprintf('Opening file...'); %print statement!
        io = imread(SVSname, 'Index', 1);
        fprintf('Opened file!'); %print statement!
        svsinfo=imfinfo(SVSname);
        height = int32(svsinfo(1).Height);
        width = int32(svsinfo(1).Width);

        [status, msg, msgID] = mkdir(folderName);
        PNGname = strcat('C:/Research/SVS/', files(i).name(1:end-4));
        PNGname = strcat(PNGname, '/');
        PNGname = strcat(PNGname, files(i).name(1:end-4));

        divL = int32(10000);

        num = idivide(width, divL,'floor')-int32(1);
        fprintf(PNGname);                         %print statement!
        fprintf('\n width:');
        fprintf(int2str(width));
        fprintf('\n');
        for j = 0: num
            %[xmin ymin width height]
            xmin = j*10000;
            J = imcrop(io, [xmin 0 divL height]);
            temp = strcat(PNGname, '_');
            temp = strcat(temp, int2str(j));
            temp = strcat(temp, '_AP.png');
            imwrite(J, temp, 'png');
            fprintf(int2str(j));                  %print statement!
            fprintf(' ');
        end
        num = num + 1;
        xmin = (num)*10000;
        tempWidth = width - xmin;

        J = imcrop(io, [xmin 0 tempWidth height]);
        temp = strcat(PNGname, '_');
        temp = strcat(temp, int2str(num));
        temp = strcat(temp, '_AP.png');
        imwrite(J, temp, 'png');
        fprintf(int2str(num));                      %print statement!
        fprintf('\n tempWidth: ');
        fprintf(int2str(tempWidth));
        fprintf('\n');                            %print statement!
    end
    fprintf("ended!!!")
end