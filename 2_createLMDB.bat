##lmdb
set EXAMPLE=./
    
#train.txt val.txt
set DATA=./
    
#caffe
set TOOLS=%CAFFE_PATH%
    
#img dir
set TRAIN_DATA_ROOT=.\croped\
  
set VAL_DATA_ROOT=.\croped\


# 
  
set RESIZE_HEIGHT=144 
set RESIZE_WIDTH=144 

  
  
echo "Creating train lmdb..."  
  
  
set GLOG_logtostderr=1 
%CAFFE_PATH%\convert_imageset --gray --resize_height=%RESIZE_HEIGHT% --resize_width=%RESIZE_WIDTH% --shuffle  %TRAIN_DATA_ROOT%    %DATA%\Basic_CNN_train_9_165.txt    %EXAMPLE%\train_lmdb  

echo "Creating val lmdb..."  
  
  
REM set GLOG_logtostderr=1 
REM %CAFFE_PATH%\convert_imageset --resize_height=%RESIZE_HEIGHT% --resize_width=%RESIZE_WIDTH% --shuffle %VAL_DATA_ROOT%  %DATA%\val.txt %EXAMPLE%/val_lmdb  
  
echo "Done." 