import sys
import torch
from torchvision import models
from PIL import Image

# Cargar la imagen
image_path = 'uploads/' + sys.argv[1]  # Ruta de la imagen cargada desde el formulario
image = Image.open(image_path)

# Convertir la imagen a tensor
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
])
image_tensor = preprocess(image).unsqueeze(0)

# Definir la arquitectura de la red (debes tener el modelo y los pesos guardados previamente)
model = models.vgg16(pretrained=False)
model.classifier[6] = nn.Linear(4096, 1)  # Asegúrate de que num_classes sea igual al número de clases que tenías cuando entrenaste el modelo

# Cargar los pesos del modelo entrenado
model.load_state_dict(torch.load('modelo_binario_entrenado2.pth'))
model.eval()

# Realizar la predicción
with torch.no_grad():
    outputs = model(image_tensor)
    predicted = torch.sigmoid(outputs) > 0.5

# Enviar el resultado de la predicción como salida estándar
print("1" if predicted.item() else "0")