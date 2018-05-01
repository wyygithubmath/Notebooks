%% OS
if ismac
    disp('Mac OS')
elseif isunix
    disp('Linux')
elseif ispc
    disp('Windows')
else
    disp('Platform not supported')
end

computer
computer('arch')

%% version
version
version -date
version -release
version -java

[v, d] = version;

ver matlab

%% system
system('pwd')