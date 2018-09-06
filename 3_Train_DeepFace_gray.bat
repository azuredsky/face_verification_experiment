mkdir log
set GLOG_logtostderr=0 
set GLOG_alsologtostderr=1 
%CAFFE_PATH%\caffe.exe train --solver=LCNN_solver.prototxt --weights=LightenedCNN_C.caffemodel --gpu=0
