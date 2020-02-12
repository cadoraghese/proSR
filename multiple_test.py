import os
import subprocess

path = 'D:\\Documents\\Workspace\\ADL_proSR\\'
input = 'D:\\Documents\\Workspace\\ADL_proSR\\data\\datasets\\open_image\\'
checkpoint = 'D:\\Documents\\Workspace\\ADL_proSR\\data\\checkpoints\\'
target = 'D:\\Documents\\Workspace\\ADL_proSR\\data\\datasets\\open_image\\'
output = 'D:\\Documents\\Workspace\\ADL_proSR\\output\\open_image\\automated\\'

text = ''
tmp_psnr = 0
scales = [4, 8]
prev_scale = 0
prev_couple = []
prev_dataset = ''

for scale in scales:
    sizes = [16, 32, 64, 128, 256, 512]
    couples = []
    for size in sizes:
        if size * scale in sizes:
            couples += [[size, size * scale]]
    for couple in couples:
        datasets = ['faces_1000', 'general_1000']
        for dataset in datasets:
            models = ['faces', 'general']
            for model in models:
                string = 'python '+path+'test.py '
                string += '--input '+input+dataset+'_'+str(couple[0])+' '
                string += '--checkpoint '+checkpoint+model+'_'+str(scale)+'x.pth'+' '
                string += '--target '+target+dataset+'_'+str(couple[1])+' '
                string += '--scale '+str(scale)+' '
                string += '--output-dir '+output+str(scale)+'x_'+str(couple[0])+'-'+str(couple[1])+'\\'+'ds_'+dataset.split('_')[0]+'-model_'+model
                print(string)
                p1 = subprocess.check_output(string)
                p1_out = p1.decode('utf-8').split('\n')[-2]
                print(p1_out)

                if model == models[1]:
                    perc = float(tmp_psnr)/float(p1_out.split(' ')[3])*100.0 - 100.0
                    text += '  ->  '+str(round(perc, 3))+'%\n'
                else:
                    text += '\n'

                if scale != prev_scale:
                    text += 'scale: {:3s} '.format(str(scale)+'x,')
                else:
                    text += ' '*11

                if couple != prev_couple:
                    text += 'sizes: {:9s}  '.format(str(couple[0])+'->'+str(couple[1])+',')
                else:
                    text += ' '*18

                if dataset != prev_dataset:
                    text += 'dataset: {:13s} '.format(dataset+',')
                else:
                    text += ' '*23

                text += 'model: {:8s}  psnr: '.format(model+';')+p1_out.split(' ')[3]
                tmp_psnr = p1_out.split(' ')[3]
                prev_scale = scale
                prev_couple = couple
                prev_dataset = dataset
                print()
                print(text)

