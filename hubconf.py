import torch
import torchvision.models as models

def fun_print():
	print("Hello World!")
	return "Hey"

model=models.vgg16(weights='IMAGENET1K_V1')
torch.save(model.state_dict(), 'model_weights.pth')

def get_model():
	print("model")
	return model