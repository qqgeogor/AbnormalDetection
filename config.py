# file config
use_all = True # 是否使用全量数据
full_path = 'kddcup.data\\kddcup.data.corrected' # 全量数据路径
ten_percent_path  = 'kddcup.data_10_percent\\kddcup.data_10_percent_corrected' # 10%数据路径
test_path = 'corrected\\corrected' # 验证集路径

train_data_path = 'kdd99.h5' # 训练数据文件目录
test_data_path = 'test_kdd99.h5' # 验证数据文件目录

scaler_path = 'scaler.pkl' # scaler文件目录

loss_type = 'H' # vbae类型，推荐H
save_path = 'vbae_AE_ATT_LightConv_%s.h5'%loss_type

## train config
train_model = True # 是否训练模型
load_model = False # 是否加载训练好模型
use_fgm = False # 控制是否使用FGM对抗攻击的方式增加模型鲁棒性
epsilon = 0.001

## model config
emb_name = ['fc_mu','fc_var']

learning_rate = 0.0005
hidden_dim = 128
beta = 10. # beta vae参数
gamma = 1000. # beta vae参数

batch_size = 128
require_improvement_epoch = 5
num_epochs = 10 
kld_weight = 0.05 # kld loss权重
