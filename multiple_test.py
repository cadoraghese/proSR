import os
import subprocess

path = 'D:\\Documents\\Workspace\\ADL_proSR\\'
input = 'D:\\Documents\\Workspace\\ADL_proSR\\data\\datasets\\open_image\\'
checkpoint = 'D:\\Documents\\Workspace\\ADL_proSR\\data\\checkpoints\\'
target = 'D:\\Documents\\Workspace\\ADL_proSR\\data\\datasets\\open_image\\'
output = 'D:\\Documents\\Workspace\\ADL_proSR\\output\\open_image\\tmp\\automated\\'

checkpoint_exist = False
text = ''
previous_psnr_old_model = 0
previous_psnr_tl_model = 0
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
            models = ['faces_test_1', 'general_test_1']

            for model in models:
                # test old
                string = 'python '+path+'test.py '
                string += '--input '+input+dataset+'_'+str(couple[0])+' '
                string += '--target '+target+dataset+'_'+str(couple[1])+' '
                string += '--checkpoint '+checkpoint+model+'_'+str(scale)+'x_net_G.pth'+' '
                string += '--output-dir '+output+str(scale)+'x_'+str(couple[0])+'-'+str(couple[1])+'\\'+'ds_'+dataset.split('_')[0]+'-model_'+model+' '
                string += '--scale '+str(scale)
                print(string)
                p1 = subprocess.check_output(string)
                p1_out = p1.decode('utf-8').split('\n')[-2]
                psnr_old_model = float(p1_out.split(' ')[3])

                # test new
                if os.path.exists(checkpoint+model+'_'+str(scale)+'x_'+str(couple[0])+'_'+str(couple[1])+'_net_G.pth'):
                    checkpoint_exist = True
                else:
                    checkpoint_exist = False

                if checkpoint_exist:
                    string = 'python '+path+'test.py '
                    string += '--input '+input+dataset+'_'+str(couple[0])+' '
                    string += '--target '+target+dataset+'_'+str(couple[1])+' '
                    string += '--checkpoint '+checkpoint+model+'_'+str(scale)+'x_'+str(couple[0])+'_'+str(couple[1])+'_net_G.pth'+' '
                    string += '--output-dir '+output+str(scale)+'x_'+str(couple[0])+'-'+str(couple[1])+'\\'+'alt-ds_'+dataset.split('_')[0]+'-model_'+model+' '
                    string += '--scale '+str(scale)
                    print(string)
                    p1 = subprocess.check_output(string)
                    p1_out = p1.decode('utf-8').split('\n')[-2]
                    psnr_tl_model = float(p1_out.split(' ')[3])

                # first line
                if prev_scale == 0:
                    text += ''

                # general (it completes faces)
                elif model == models[1]:
                    text += 'psnr: {:5.2f}'.format(previous_psnr_old_model)
                    # add first perc
                    perc = previous_psnr_old_model / psnr_old_model * 100.0 - 100.0
                    text += '  ->  {:6.3f}%'.format(perc)
                    # add second perc
                    perc = 10 ** ((previous_psnr_old_model-psnr_old_model)/10) * 100.0 - 100.0
                    text += '   {:5.2f}%   '.format(perc)

                    if checkpoint_exist and prev_checkpoint_exist:
                        text += 'psnr: {:5.2f}'.format(previous_psnr_tl_model)
                        # add first perc
                        perc = previous_psnr_tl_model / psnr_tl_model * 100.0 - 100.0
                        text += '  ->  {:6.3f}%'.format(perc)
                        # add second perc
                        perc = 10 ** ((previous_psnr_tl_model-psnr_tl_model)/10) * 100.0 - 100.0
                        text += '   {:5.2f}%\n'.format(perc)
                    else:
                        text += '\n'

                # faces (it completes general)
                else:
                    text += 'psnr: {:5.2f}'.format(previous_psnr_old_model)
                    text += ' '*25
                    if prev_checkpoint_exist:
                        text += 'psnr: {:5.2f}\n'.format(previous_psnr_tl_model)
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

                text += 'model: {:8s}  '.format(model + ';')

                previous_psnr_old_model = psnr_old_model
                if checkpoint_exist:
                    previous_psnr_tl_model = psnr_tl_model
                prev_scale = scale
                prev_couple = couple
                prev_dataset = dataset
                prev_checkpoint_exist = checkpoint_exist

text += 'psnr: {:5.2f}'.format(previous_psnr_old_model)
text += ' ' * 25
if checkpoint_exist:
    text += 'psnr: {:5.2f}\n'.format(previous_psnr_tl_model)
print()
print(text)

