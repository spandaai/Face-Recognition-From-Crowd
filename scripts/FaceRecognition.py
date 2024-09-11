from scripts.DatabaseHandle import DatabaseHandler
import json
import cv2
from scripts.FRMethods.ContractiveLossFR import ContractiveLossFR
from scripts.FRMethods.SingleShotLearningFR import (
    SSLFacentDataModule,
    SingleShotLearningFR,
)
from scripts.Upsample import Upsample
from scripts.FRMethods.ContractiveLossFR import (
    ContractiveLossFR,
    ContractiveLossFREmbeddingsDataModule,
)
from PIL import Image
from torchvision import transforms
import torch
import torch.nn.functional as F
import pytorch_lightning as pl
from utils import utils
import numpy as np

"@Author: NavinKumarMNK"
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class Predictor:
    def __init__(self, file=False, label=True):
        self.label = label
        self.upsample = Upsample()  # Instance variable defined in __init__
        self.file = file
        self.model = SingleShotLearningFR(pretrained=True)
        args = utils.config_parse("CONTRACTIVE_LOSS_FR")
        args["num_classes"] = len(os.listdir(utils.ROOT_PATH + "/database/faces"))
        self.embedding = ContractiveLossFR(**args, pretrained=True)
        self.model = self.model.to(DEVICE)

    def upsampler(self, image, file=False):
        try:
            self.upsample.set_image(image, 0.5, file)
            self.upsample.denoising()
        except Exception as e:
            print(f"Error in upsampling: {e}")

    def predict(self, image):
        # Example function for predicting using the model
        image = transforms.ToTensor()(image).unsqueeze(0).to(DEVICE)
        with torch.no_grad():
            prediction = self.model(image)
        return torch.argmax(prediction, dim=1)

