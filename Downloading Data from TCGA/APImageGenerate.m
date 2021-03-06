fileID = fopen('C:/KavyaFiles/patchesListFinal.txt', 'r');
formatSpec = '%s';
sizeS = [Inf];
fileInput = fscanf(fileID, formatSpec, sizeS);
s = strsplit(fileInput, ',');
counter = 1;
missed = 0;
fprintf('starting!! ');
for temp = 1: length(s)
    totalFileName = s{counter};
    
    splitArr = strsplit(totalFileName, '_');
    fileName = splitArr{1};
    
    t1 = strcat('C:/Research/SVSFiles/', fileName);
    t1 = strcat(t1, '.svs');
    
    if exist(t1, 'file') ~= 2
        missed = missed + 1;
    end
    if exist(t1, 'file') == 2
        fprintf('Opening file...');                             %print statement!
        io = imread(t1, 'Index', 1);
        fprintf('Opened file!');                                %print statement!

        i = str2num(splitArr{2});
        j = str2num(splitArr{3});
        xmin = i*256;
        ymin = j*256;    
        %[xmin ymin width height]
        J = imcrop(io, [xmin ymin 255 255]);
        
        t3 = totalFileName(1:end-7);
        t2 = strcat(strcat('C:/Research/APPatches/', t3), '_AP.png');
        
        imwrite(J,t2, 'png');
        fprintf("saved");

        nextTotalFileName = s{counter+1};
        nextSplitArr = strsplit(nextTotalFileName, '_');
        nextFileName = nextSplitArr{1};

        while(strcmp(nextFileName, fileName) == 1)
            counter = counter + 1;
            fprintf('counter: ');
            fprintf(string(counter));                                    %print statement!
            fprintf(' missed: ');
            fprintf(string(missed));
            fprintf(t3);            
            fprintf('\n');
            
            totalFileName = s{counter};
            t3 = totalFileName(1:end-7);
            splitArr = strsplit(totalFileName, '_');
            fileName = splitArr{1};
            i = str2num(splitArr{2});
            j = str2num(splitArr{3});

            xmin = i*256;
            ymin = j*256;    
            %[xmin ymin width height]
            J = imcrop(io, [xmin ymin 255 255]);
            t2 = strcat(strcat('C:/Research/APPatches/', t3), '_AP.png');
            imwrite(J, t2, 'png');
            nextTotalFileName = s{counter+1};
            nextSplitArr = strsplit(nextTotalFileName, '_');
            nextFileName = nextSplitArr{1};
        end
        counter = counter + 1;
    end
    counter = counter + 1;
end
fclose(fileID);