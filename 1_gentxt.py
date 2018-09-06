import os

def caffe_input_txt_maker(data_folder,outfile_name, phase = 'train'):
    # 计数文件个数
    file_cnt = 0
    class_cnt = 0
    label_uniq_cnt={}
    with open(outfile_name,'w', encoding="utf-8") as fobj:

            for file_name in os.listdir(data_folder):
                file_cnt +=1
                label = file_name.split('_')[0]
                label = label.split('*.jpg')[0]
                
                if label not in label_uniq_cnt:
                    label_uniq_cnt[label]=0
                    class_cnt=class_cnt + 1
                label_uniq_cnt[label]=label_uniq_cnt[label]+1
                
                # 将文件夹名称也添加入内
                if phase == 'train' :
                    file_path = file_name

                if phase == 'test' :
                    file_path = file_name

                fobj.writelines( file_path +" "*5+str(class_cnt-1)+'\n')

    file_dir, base_name = os.path.split(outfile_name)
    file_name, ext = os.path.splitext(base_name)

    new_outfile_name = file_dir + '/' + file_name + '_%d_%d' % (len(label_uniq_cnt), file_cnt) + ext
    if os.path.exists(new_outfile_name):
        os.remove(new_outfile_name)
    os.rename(outfile_name, new_outfile_name)
    print ('Done')
    print(label_uniq_cnt)


if __name__ == "__main__":
    caffe_input_txt_maker(data_folder = './croped',
                         outfile_name = "./Basic_CNN_train.txt", phase = 'train')

    # caffe_input_txt_maker(data_folder = 'd:/WORKSPACE/DATA/caffe_test_data/test',
                         # outfile_name = "./Basic_CNN_test.txt", phase = 'test')