import torch
 
model_dict = torch.load("./model/trial_wwj_2_ave/checkpoints/ngp_ep0036.pth")
params_dict = model_dict['state_dict']
 
total_params = 0
for param_tensor in params_dict.values():
    # 将当前参数的元素数（即参数大小）加到总和中
    total_params += param_tensor.numel()
 
print(f"参数量约为：{total_params/1000000:.2f}M（百万个参数）。")